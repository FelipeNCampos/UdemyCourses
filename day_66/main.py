from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from werkzeug.exceptions import HTTPException

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


def parse_bool(value):
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def get_request_value(field):
    if request.is_json:
        json_data = request.get_json(silent=True) or {}
        if field in json_data:
            return json_data[field]
    if field in request.form:
        return request.form.get(field)
    if field in request.args:
        return request.args.get(field)
    return None


def serialize_cafe(cafe):
    return {
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "can_take_calls": cafe.can_take_calls,
        "coffee_price": cafe.coffee_price,
    }


def error_response(message, status_code):
    return jsonify(error={"message": message}), status_code


# Cafe TABLE Configuration
class Cafe(db.Model): 
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify(error={
        "code": error.code,
        "name": error.name,
        "message": error.description,
    }), error.code


@app.errorhandler(Exception)
def handle_unexpected_exception(error):
    app.logger.exception("Unhandled exception: %s", error)
    return jsonify(error={"message": "Internal server error"}), 500


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    cafe = db.session.query(Cafe).order_by(db.func.random()).first()
    if cafe:
        return jsonify(cafe=serialize_cafe(cafe))
    return error_response("No cafes found in the database.", 404)


# HTTP GET - Read Record
@app.route("/cafe")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[serialize_cafe(cafe) for cafe in cafes])

@app.route("/cafe/<int:cafe_id>")
def get_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        return jsonify(cafe=serialize_cafe(cafe))
    else:
        return error_response("Sorry, a cafe with that id was not found in the database.", 404)



@app.route("/search")
def search_cafes():
    location = request.args.get("loc")
    if not location:
        return error_response("Missing required query parameter: loc", 400)

    cafes = db.session.query(Cafe).filter(Cafe.location.ilike(f"%{location}%")).all()
    if cafes:
        return jsonify(cafes=[serialize_cafe(cafe) for cafe in cafes])
    else:
        return error_response("Sorry, we couldn't find any cafes at that location.", 404)

# HTTP POST - Create Record

@app.route("/cafe", methods=["POST"])
def create_cafe():
    required_fields = ["name", "map_url", "img_url", "location", "seats"]
    missing_fields = [field for field in required_fields if not request.form.get(field)]
    if missing_fields:
        return error_response(f"Missing required field(s): {', '.join(missing_fields)}", 400)

    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=parse_bool(request.form.get("has_toilet")),
        has_wifi=parse_bool(request.form.get("has_wifi")),
        has_sockets=parse_bool(request.form.get("has_sockets")),
        can_take_calls=parse_bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(message="Cafe added successfully", cafe=serialize_cafe(new_cafe)), 201

# HTTP PUT/PATCH - Update Record
@app.route("/cafe/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        text_fields = ["name", "map_url", "img_url", "location", "seats", "coffee_price"]
        bool_fields = ["has_toilet", "has_wifi", "has_sockets", "can_take_calls"]

        for field in text_fields:
            value = get_request_value(field)
            if value is not None:
                setattr(cafe, field, value)

        for field in bool_fields:
            value = get_request_value(field)
            if value is not None:
                setattr(cafe, field, parse_bool(value))
        
        db.session.commit()
        return jsonify(message="Cafe updated successfully", cafe=serialize_cafe(cafe)), 200
    else:
        return error_response("Sorry, a cafe with that id was not found in the database.", 404)


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = get_request_value("new_price")
    if new_price is None or str(new_price).strip() == "":
        return error_response("Missing required parameter: new_price", 400)

    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return error_response("Sorry, a cafe with that id was not found in the database.", 404)

# HTTP DELETE - Delete Record
@app.route("/cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(message="Cafe deleted successfully"), 200
    else:
        return error_response("Sorry, a cafe with that id was not found in the database.", 404)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import requests
import smtplib
import dotenv
from email.message import EmailMessage

vars = dotenv.dotenv_values(".env")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/a1396bec1668e0423abd").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact", methods=["POST"])
def contact_post():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    msg = EmailMessage()
    msg["Subject"] = f"New message from {name}"
    msg["From"] = vars["EMAIL"]
    msg["To"] = email
    msg.set_content(f"{message}")

    loginvars = {
        "EMAIL": str(vars["EMAIL"]),
        "APP-PASSWORD": str(vars["APP-PASSWORD"])
    }
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=loginvars["EMAIL"], password=loginvars["APP-PASSWORD"])
        connection.send_message(msg)
        
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Optional
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    all_posts = db.session.query(BlogPost).all()
    posts = []
    for post in all_posts:
        posts.append(post)
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.session.query(BlogPost).filter_by(id=post_id).first()
    return render_template("post.html", post=requested_post)


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class EditPostForm(FlaskForm):
    title = StringField("Blog Post Title")
    subtitle = StringField("Subtitle")
    author = StringField("Your Name")
    img_url = StringField("Blog Image URL", validators=[Optional(), URL()])
    body = CKEditorField("Blog Content")
    submit = SubmitField("Update Post")

@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():

    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=date.today().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    form = EditPostForm()
    post = db.session.query(BlogPost).filter_by(id=post_id).first()
    if not post:
        return "Post not found", 404
    if form.validate_on_submit():
        if form.title.data:
            post.title = form.title.data
        if form.subtitle.data:
            post.subtitle = form.subtitle.data
        if form.body.data:
            post.body = form.body.data
        if form.author.data:
            post.author = form.author.data
        if form.img_url.data:
            post.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=form, post=post)


@app.route('/delete-post/<int:post_id>', methods=["POST"])
def delete_post(post_id):
    post = db.session.query(BlogPost).filter_by(id=post_id).first()
    if not post:
        return "Post not found", 404
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

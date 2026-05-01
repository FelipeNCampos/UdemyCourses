from flask import Flask, render_template
from post import Post

app = Flask(__name__)
posts = Post()

@app.route('/')
def home():
    all_posts = posts.get_data()
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post_data = posts.get_post_data(post_id)
    return render_template("post.html", post=post_data)

if __name__ == "__main__":
    app.run(debug=True)

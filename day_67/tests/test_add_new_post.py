import importlib.util
from pathlib import Path


def load_main_module():
    main_path = Path(__file__).resolve().parents[1] / "main.py"
    spec = importlib.util.spec_from_file_location("blog_main", main_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_add_new_post_saves_submitted_post_and_redirects(monkeypatch):
    main = load_main_module()
    saved_posts = []
    monkeypatch.setattr(main.db.session, "add", saved_posts.append)
    monkeypatch.setattr(main.db.session, "commit", lambda: None)

    response = main.app.test_client().post(
        "/new-post",
        data={
            "title": "A title",
            "subtitle": "A subtitle",
            "author": "An author",
            "img_url": "https://example.com/image.jpg",
            "body": "Post body",
        },
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")
    assert len(saved_posts) == 1
    assert saved_posts[0].title == "A title"
    assert saved_posts[0].subtitle == "A subtitle"
    assert saved_posts[0].author == "An author"
    assert saved_posts[0].img_url == "https://example.com/image.jpg"
    assert saved_posts[0].body == "Post body"

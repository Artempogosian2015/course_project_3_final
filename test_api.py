from main import app


def text_posts():
    response = app.test_client().get('/api/post/')
    assert isinstance(response.json, list)
    assert response.status_code == 200


def text_post():
    response = app.test_client().get('/api/post/1')
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
                                         'pk'}
    assert response.status_code == 200

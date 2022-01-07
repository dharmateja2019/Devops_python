from ap import app


def test_home1():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_home2():
    response = app.test_client().get('/edit')
    assert response.status_code == 200

"""This test the homepage"""
import os


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data


def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert b"welcome" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404


def test_request_about_with_debug_file(client):
    """This that when we make a request to a page,
    a debug file is made"""
    root = os.path.dirname(os.path.abspath(__file__))
    logs = os.path.join(root, '../app/logs/debug.log')
    os.remove(logs)
    assert os.path.isfile(logs) is False
    client.get("/about")
    assert os.path.isfile(logs) is True


def test_request_about_with_request_log_file(client):
    """This that when we make a request to a page,
    an info file is made"""
    root = os.path.dirname(os.path.abspath(__file__))
    logs = os.path.join(root, '../app/logs/flask.log')
    os.remove(logs)
    assert os.path.isfile(logs) is False
    client.get("/about")
    assert os.path.isfile(logs) is True

"""This tests the generation of log files"""
import os


def test_request_about_with_debug_file(client):
    """This tests that when we make a request to a page,
    a debug file is made"""
    root = os.path.dirname(os.path.abspath(__file__))
    logs = os.path.join(root, '../app/logs/debug.log')
    os.remove(logs)
    assert os.path.isfile(logs) is False
    client.get("/about")
    assert os.path.isfile(logs) is True


def test_request_about_with_flask_and_request_log_file(client):
    """This tests that when we make a request to a page,
    an info file is made"""
    root = os.path.dirname(os.path.abspath(__file__))
    flask_logs = os.path.join(root, '../app/logs/flask.log')
    request_logs = os.path.join(root, '../app/logs/request.log')
    os.remove(flask_logs)
    os.remove(request_logs)
    assert os.path.isfile(flask_logs) is False
    assert os.path.isfile(request_logs) is False
    client.get("/about")
    assert os.path.isfile(flask_logs) is True
    assert os.path.isfile(request_logs) is True

from nose.tools import assert_true
import requests


def test_request_response():
    response = requests.get('/login')
    assert_true(response.ok)
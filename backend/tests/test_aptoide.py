import falcon # type: ignore
from falcon import testing
import pytest

from src.app import app

API_ERROR_RESPONSES = {
    'missing_url': (falcon.HTTP_400, {'error': '"url" query parameter is required.'}),
    'invalid_url': (falcon.HTTP_400, {'error': 'Invalid Aptoide URL.'}),
    'not_found': (falcon.HTTP_404, {'error': 'App not found.'}),
    'server_error': (falcon.HTTP_500, {'error': 'Something went wrong.'}),
}

@pytest.fixture
def client():
    return testing.TestClient(app)

def test_GET_aptoide_url_valid(client):
    url = 'https://magicabin.en.aptoide.com/app'

    response = client.simulate_get(f'/api/aptoide?url={url}')
    result = response.json

    assert response.status == falcon.HTTP_200
    assert type(result) == dict

    # Check if the response contains the expected keys and values as strings
    expected_keys = ['name', 'icon_url', 'version', 'num_downloads', 'release_date', 'description']
    assert all(key in result and type(result[key]) == str for key in expected_keys)

def test_GET_aptoide_url_missing_url_parameter(client):
    response = client.simulate_get('/api/aptoide')
    result = response.json

    expected = API_ERROR_RESPONSES['missing_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_missing_https(client):
    url = 'magicabin.en.aptoide.com/app'

    response = client.simulate_get(f'/api/aptoide?url={url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_missing_language(client):
    url = 'https://magicabin.aptoide.com/'

    response = client.simulate_get(f'/api/aptoide?url={url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_nonexistent_app(client):
    url = 'https://fakeappdoesnotexist.en.aptoide.com/app'

    response = client.simulate_get(f'/api/aptoide?url={url}')
    result = response.json

    expected = API_ERROR_RESPONSES['not_found']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_nonexistent_language(client):
    url = 'https://magicabin.fakelanguage123.aptoide.com/app'

    response = client.simulate_get(f'/api/aptoide?url={url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_other_url(client):
    url = 'https://www.google.com'

    response = client.simulate_get(f'/api/aptoide?url={url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_not_url(client):
    url = 'SELECT * FROM users'

    response = client.simulate_get(f'/api/aptoide?url={url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]
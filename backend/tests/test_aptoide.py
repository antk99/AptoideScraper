import falcon
from falcon import testing
import pytest

from src.app import app

API_ERROR_RESPONSES = {
    'missing_url': (falcon.HTTP_400, {'error': '"url" query parameter is required.'}),
    'invalid_url': (falcon.HTTP_400, {'error': 'Invalid Aptoide URL.'}),
    'not_found': (falcon.HTTP_404, {'error': 'App not found.'}),
    'server_error': (falcon.HTTP_500, {'error': 'Something went wrong.'}),
}

GET_APTOIDE_API_BASE_URL = '/api/aptoide?url='

@pytest.fixture
def client() -> testing.TestClient:
    return testing.TestClient(app)

def test_GET_aptoide_url_valid(client: testing.TestClient) -> None:
    url = 'https://instagram.en.aptoide.com/app'

    response = client.simulate_get(f'{GET_APTOIDE_API_BASE_URL}{url}')
    result = response.json

    assert response.status == falcon.HTTP_200
    assert type(result) == dict

    # Check if the response contains the expected keys and values as strings
    expected_keys = ['name', 'icon_url', 'version', 'num_downloads', 'release_date', 'description']
    assert all(key in result and type(result[key]) == str for key in expected_keys)
    assert result['name'] == 'Instagram'

def test_GET_aptoide_url_missing_url_parameter(client: testing.TestClient) -> None:
    response = client.simulate_get('/api/aptoide')
    result = response.json

    expected = API_ERROR_RESPONSES['missing_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_missing_https(client: testing.TestClient) -> None:
    url = 'instagram.en.aptoide.com/app'

    response = client.simulate_get(f'{GET_APTOIDE_API_BASE_URL}{url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_missing_language(client: testing.TestClient) -> None:
    url = 'https://instagram.aptoide.com/'

    response = client.simulate_get(f'{GET_APTOIDE_API_BASE_URL}{url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_nonexistent_app(client: testing.TestClient) -> None:
    url = 'https://fakeappdoesnotexist.en.aptoide.com/app'

    response = client.simulate_get(f'{GET_APTOIDE_API_BASE_URL}{url}')
    result = response.json

    expected = API_ERROR_RESPONSES['not_found']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_nonexistent_language(client: testing.TestClient) -> None:
    url = 'https://instagram.fakelanguage123.aptoide.com/app'

    response = client.simulate_get(f'{GET_APTOIDE_API_BASE_URL}{url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_invalid_other_url(client: testing.TestClient) -> None:
    url = 'https://www.google.com'

    response = client.simulate_get(f'{GET_APTOIDE_API_BASE_URL}{url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]

def test_GET_aptoide_url_not_url(client: testing.TestClient) -> None:
    url = 'SELECT * FROM users'

    response = client.simulate_get(f'{GET_APTOIDE_API_BASE_URL}{url}')
    result = response.json

    expected = API_ERROR_RESPONSES['invalid_url']
    assert response.status == expected[0] and result == expected[1]
from fastapi.testclient import TestClient
from .main import app, get_settings
from .src import Settings

client = TestClient(app)


def get_settings_override():
    return Settings(MARKEY_URL="https://australQA.markey.com.ar/APIMarkeyV2/obtener",
                    MARKEY_TOKEN='UZN9291llgxWJ93uzilrmantG6t20r0v8kwrihYXmZl1EO8irdhT0gFK0tFAlv3m',
                    MARKEY_API_KEY="933ec3bb-91c7-4ca5-bcdd-5220778c0f36",
                    CUSTOMERTYPE=829,
                    NO_CUSTOMERTYPE=799)


# Cambio las credenciales por las de testing
app.dependency_overrides[get_settings] = get_settings_override


def test_main():
    response = client.post("/markey", json={"dni": "valentinpugliese"})
    assert response.status_code == 200


def test_main_broken():
    response = client.post("/markey", json={"dni": 420})
    assert response.status_code == 422


def test_main_not_null():
    response = client.post("/markey", json={"dni": "1"})
    assert len(response.text) > 0

import os
import pytest  # type: ignore
import requests

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BOOKER_BASE_URL", "https://restful-booker.herokuapp.com")



@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    return s


@pytest.fixture(scope="session")
def auth_token(session, base_url):
    r = session.post(f"{base_url}/auth", json={"username": "admin", "password": "password123"})
    assert r.status_code == 200
    return r.json()["token"]


@pytest.fixture
def booking_payload():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-01-10", "checkout": "2026-01-12"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking_id(session, base_url, booking_payload):
    r = session.post(f"{base_url}/booking", json=booking_payload)
    assert r.status_code == 200
    return r.json()["bookingid"]

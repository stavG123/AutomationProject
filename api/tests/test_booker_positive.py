def test_create_booking_200(session, base_url, booking_payload):
    r = session.post(f"{base_url}/booking", json=booking_payload)
    assert r.status_code == 200
    data = r.json()
    assert "bookingid" in data
    assert data["booking"]["firstname"] == booking_payload["firstname"]


def test_get_booking_200(session, base_url, created_booking_id):
    r = session.get(f"{base_url}/booking/{created_booking_id}")
    assert r.status_code == 200
    body = r.json()
    assert "firstname" in body
    assert "lastname" in body


def test_update_booking_200(session, base_url, created_booking_id, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}",
    }

    payload = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 555,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-02-01", "checkout": "2026-02-03"},
        "additionalneeds": "Late checkout",
    }

    r = session.put(f"{base_url}/booking/{created_booking_id}", json=payload, headers=headers)
    assert r.status_code == 200
    assert r.json()["firstname"] == "Jane"
    assert r.json()["totalprice"] == 555


def test_delete_booking_201(session, base_url, created_booking_id, auth_token):
    headers = {"Cookie": f"token={auth_token}"}
    r = session.delete(f"{base_url}/booking/{created_booking_id}", headers=headers)
    assert r.status_code == 201

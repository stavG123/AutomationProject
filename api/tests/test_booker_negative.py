def test_update_without_token_403(session, base_url, created_booking_id):
    payload = {
        "firstname": "No",
        "lastname": "Token",
        "totalprice": 1,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-03-01", "checkout": "2026-03-02"},
        "additionalneeds": "None",
    }

    r = session.put(f"{base_url}/booking/{created_booking_id}", json=payload)
    assert r.status_code == 403


def test_create_booking_missing_field_400_or_500(session, base_url):
    bad_payload = {"firstname": "OnlyFirstName"}  # missing required fields
    r = session.post(f"{base_url}/booking", json=bad_payload)
    assert r.status_code in (400, 500)


def test_wrong_content_type_400_415_500(session, base_url):
    headers = {"Content-Type": "text/plain"}
    r = session.post(f"{base_url}/booking", data="not json", headers=headers)
    assert r.status_code in (400, 415, 500)

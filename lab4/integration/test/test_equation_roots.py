import requests
from ..default_values import body_equation_roots


def test_validation_eqaution_roots(equation_roots_url: str):
    payload = body_equation_roots.copy()
    for key in body_equation_roots:
        payload.pop(key)
        r = requests.post(equation_roots_url, json=payload)
        assert r.status_code == 422
    payload = body_equation_roots.copy()
    payload.update(a="True",
                   b="",
                   c=False)
    r = requests.post(equation_roots_url, json=payload)
    assert r.status_code == 422


def test_get_eq_roots(equation_roots_url: str):
    payload = body_equation_roots.copy()
    r = requests.post(equation_roots_url, json=payload)
    assert r.status_code == 200
    result = r.json()
    assert result.get("success")
    assert result.get("message") is None
    assert len(result.get("data")) == 2


def test_get_eq_roots_neg_1(equation_roots_url: str):
    payload = body_equation_roots.copy()
    payload.update(a=1,
                   b=1,
                   c=1)
    r = requests.post(equation_roots_url, json=payload)
    assert r.status_code == 200
    result = r.json()
    assert len(result.get("data")) == 0
    assert result.get("success")
    assert result.get("message").strip() == "Not Found"


def test_get_eq_roots_neg_2(equation_roots_url):
    payload = body_equation_roots.copy()
    payload.update(a=0,
                   b=5,
                   c=1)
    r = requests.post(equation_roots_url, json=payload)
    assert r.status_code == 200
    result = r.json()
    assert len(result.get("data")) == 0
    assert result.get("success")
    assert result.get("message").strip() == "When calculating the roots, there was an attempt to divide by 0"

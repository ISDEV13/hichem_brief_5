import pytest
from fastapi.testclient import TestClient
from main import app


# --- Tests fonctionnels : on teste l'API comme un vrai utilisateur via HTTP ---

@pytest.fixture
def client():
    return TestClient(app)


def test_carre_valide(client):
    response = client.post("/carre/", json={"nombre": 5})
    assert response.status_code == 200
    assert response.json() == {"nombre": 5.0, "carre": 25.0}


def test_carre_negatif(client):
    response = client.post("/carre/", json={"nombre": -4})
    assert response.status_code == 200
    assert response.json()["carre"] == 16.0


def test_carre_zero(client):
    response = client.post("/carre/", json={"nombre": 0})
    assert response.status_code == 200
    assert response.json()["carre"] == 0.0


def test_nombre_trop_grand(client):
    response = client.post("/carre/", json={"nombre": 2_000_000})
    assert response.status_code == 422


def test_nombre_infini(client):
    response = client.post("/carre/", json={"nombre": float("inf")})
    assert response.status_code == 422


def test_champ_manquant(client):
    response = client.post("/carre/", json={})
    assert response.status_code == 422


def test_type_invalide(client):
    response = client.post("/carre/", json={"nombre": "abc"})
    assert response.status_code == 422


def test_route_inexistante(client):
    response = client.get("/route_qui_nexiste_pas")
    assert response.status_code == 404

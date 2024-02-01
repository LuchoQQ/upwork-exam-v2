from fastapi.testclient import TestClient
from app.main import app
import pytest

@pytest.fixture
def client():
    return TestClient(app)


# test create user
@pytest.fixture
def test_user():
    return {
        "email": "test@example.com",
    }

@pytest.fixture
def test_profile():
    return {
        "name": "Test Profile",
        "description": "A test profile"
    }

def test_create_user(client, test_user):
    response = client.post("/users/", json=test_user)  # Adjust the path if different in your app
    data = response.json()

    assert response.status_code == 200
    assert "user_id" in data
    assert data["message"] == "User created successfully"



def test_add_profile_to_user(client, test_user, test_profile):
    # Crear un usuario
    user_response = client.post("/users/", json=test_user)
    assert user_response.status_code == 200
    user_data = user_response.json()
    user_id = user_data["user_id"]  # Asume que el endpoint retorna un 'user_id'

    # Configura el user_id en el perfil
    profile_to_add = test_profile.copy()
    profile_to_add["user_id"] = user_id

    # Prueba agregar el perfil al usuario
    profile_response = client.put(f"/users/{user_id}/add_profile", json=profile_to_add)
    assert profile_response.status_code == 200
    profile_data = profile_response.json()
    assert profile_data["message"] == "Profile added successfully"
    assert any(p["name"] == profile_to_add["name"] for p in profile_data["user"]["profiles"])



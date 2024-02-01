import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def signup_url():
    return reverse('signup')

@pytest.fixture
def login_url():
    return reverse('token_obtain')

@pytest.fixture
def me_url():
    return reverse('me')

@pytest.fixture
def refresh_url():
    return reverse('token_refresh')

@pytest.fixture
def user_data():
    return {'email': 'test@example.com', 'name': 'TestUser', 'password': 'password123'}

@pytest.fixture
def create_user(db, user_data):
    return User.objects.create_user(**user_data)

@pytest.fixture
def access_token(api_client, login_url, user_data):
    response = api_client.post(login_url, user_data)
    assert response.status_code == 200, f"Login failed with status code {response.status_code}"
    return response.data['access']

@pytest.mark.django_db
def test_signup(api_client, signup_url, user_data):
    response = api_client.post(signup_url, user_data)
    assert response.status_code == 200

@pytest.mark.django_db
def test_login(api_client, login_url, create_user, access_token):
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    me_url = reverse('me')
    response = api_client.get(me_url)
    assert response.status_code == 200
    assert 'email' in response.json()

@pytest.mark.django_db
def test_token_refresh(api_client, refresh_url, create_user, access_token):
    # Pobierz użytkownika utworzonego za pomocą fixture
    user = create_user

    # Dodaj odpowiednie uprawnienia użytkownikowi (dostosuj według potrzeb)
    user.is_staff = True
    user.save()

    # Utwórz nowy access token dla użytkownika
    api_client.force_authenticate(user)
    refresh_token = RefreshToken.for_user(user)
    access_token = str(refresh_token.access_token)

    # Wydrukuj token dostępu dla celów debugowania
    print(f"Access Token: {access_token}")

    # Wykonaj żądanie odświeżenia tokenu
    data = {'refresh': access_token}
    response = api_client.post(refresh_url, data)

    # Sprawdź kod statusu odpowiedzi
    assert response.status_code == 200

    # Sprawdź, czy w odpowiedzi znajduje się nowy token dostępu
    assert 'access' in response.data

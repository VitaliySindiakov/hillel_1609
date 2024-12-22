import logging
import pytest
import requests
from requests import Response

logging.basicConfig(
    filename="test_search.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    force=True
)

logger = logging.getLogger("test_logger")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)


class CarAPI:
    __access_token: str = None
    __base_url: str = "http://127.0.0.1:8080"
    __user: dict = {"username": "test_user", "password": "test_pass"}

    @classmethod
    def auth(cls) -> Response:
        logger.info("Authorization")
        response: Response = requests.post(
            url=f"{cls.__base_url}/auth",
            auth=(cls.__user["username"], cls.__user["password"]))
        cls.__access_token = response.json().get("access_token")
        return response

    @classmethod
    def find_car(cls, params: dict) -> Response:
        headers = {"Authorization": f"Bearer {CarAPI.get_token()}"}
        logger.info(f"Searchin Car with params={params}")
        return requests.get(
            url=f"{cls.__base_url}/cars",
            headers=headers, params=params)

    @classmethod
    def get_token(cls):
        if not cls.__access_token:
            cls.auth()

        logger.info("Getting token")
        return cls.__access_token

@pytest.fixture(scope="class")
def test_login():
    response = CarAPI.auth()
    assert response.status_code == 200
    assert len(response.json().get("access_token")) > 0


@pytest.mark.parametrize("sort_by, limit", [
    ("brand", 5),
    ("year", 10),
    ("engine_volume", 7),
    ("price", 2),
    ("year", None),
    (None, 3),
])
def test_find_car(sort_by, limit):
    params = {"sort_by": sort_by, "limit": limit}
    response = CarAPI.find_car(params)
    cars = response.json()
    assert response.status_code == 200
    if limit is not None:
        assert len(cars) == limit

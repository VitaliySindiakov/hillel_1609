import os
import pytest
from Image_ctrl import ImageCtrl

current_dir = os.path.dirname(__file__)


@pytest.mark.parametrize("image_name", [("example.jpg")])
def test_upload(image_name):
    file_path = os.path.join(current_dir, "images", image_name)
    image_url: str = ImageCtrl().upload_image(file_path)
    assert image_name in image_url


@pytest.mark.parametrize("image_name", [("example.jpg")])
def test_get_image_url(image_name):
    headers = {'Content-Type': "text"}
    response = ImageCtrl().get_image(image_name, headers)
    assert response.status_code == 200
    assert image_name in response.json()["image_url"]


@pytest.mark.parametrize("image_name", [("example.jpg")])
def test_get_image_json(image_name):
    headers = {'Content-Type': "image"}
    response = ImageCtrl().get_image(image_name, headers)
    assert response.status_code == 200


@pytest.mark.parametrize("image_name", [("example.jpg")])
def test_delete_image(image_name):
    response = ImageCtrl().delete_image(image_name)
    message = response.json()["message"]
    assert response.status_code == 200
    assert f'Image {image_name} deleted' in message
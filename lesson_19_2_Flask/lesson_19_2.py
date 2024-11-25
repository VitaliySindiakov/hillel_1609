import os
from Image_ctrl import ImageCtrl

current_dir = os.path.dirname(__file__)


def test_upload():
    file_path = os.path.join(current_dir, "images", "example.jpg")
    image_url: str = ImageCtrl().upload_image(file_path)
    assert "image" in image_url


def test_get_image_url():
    headers = {'Content-Type': "text"}
    image_url: str = ImageCtrl().get_image_url("image", headers)
    assert "image" in image_url


def test_delete_image():
    response = ImageCtrl().delete_image("image")
    assert response == 200

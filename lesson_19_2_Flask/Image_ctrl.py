import requests


class ImageCtrl:
    def __init__(self, url="http://127.0.0.1:8080"):
        self.url = url

    def upload_image(self, image_path):
        with open(image_path, "rb") as image_file:
            data = {"image": image_file.read()}

        response = requests.post(f"{self.url}/upload", files=data)
        if response.status_code != 201:
            print("Image isn't downloaded")
        return response.json()["image_url"]

    def get_image_url(self, filename, headers=None):
        response = requests.get(f"{self.url}/image/{filename}", headers=headers)
        return response.json()["image_url"]

    def delete_image(self, filename):
        response = requests.delete(f"{self.url}/delete/{filename}")
        return response.json()

    if __name__ == "__main__":
        pass

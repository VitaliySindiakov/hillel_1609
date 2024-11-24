import requests
import pytest


@pytest.mark.parametrize("url, params", [
    ('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos',
     {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'})
])
def test_download_photo(url, params):
    response = requests.get(url, params=params)
    assert response.status_code == 200
    data = response.json()
    photos = data.get('photos', [])
    counter = 1
    for photo in photos:
        img_url = photo.get('img_src')
        with open("mars_photo" + str(counter) + ".jpg", "wb") as file:
            counter += 1
            img_response = requests.get(img_url)
            assert img_response.status_code == 200
            file.write(img_response.content)

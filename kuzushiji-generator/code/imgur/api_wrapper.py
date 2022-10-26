import requests
import os

class ImgurAPIWrapper(object):
    def __init__(self):
        self.client_id = os.environ.get('IMGUR_CLIENT_ID')
        self.client_secret = os.environ.get('IMGUR_CLIENT_SECRET')

    def upload_image(self, image):
        url = 'https://api.imgur.com/3/image'
        headers = {
            'Authorization': f'Client-ID {self.client_id}'
        }
        data = {
            'image': image
        }
        response = requests.post(url, headers=headers, data=data)
        return response.json()
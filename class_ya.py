import requests
from pprint import pprint


class YaUploader:
    token = ''
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Athorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        pprint(response.json())

    def upload(self, file_path):
        """Метод получает ссылку на загрузку"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json)
        return response.json().get('href')

    def upload_file(self, file_path, filename):
        result = self.upload(file_path=file_path)
        href = result.get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.riase_for_status()
        if response.status_code == 201:
           print('success')    
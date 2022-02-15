import requests

from pprint import pprint

class YaUploader:
    def __init__(self, token):
        self.token = token
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def _get_uploud_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()
    def upload(self, disk_file_path, filename):
        link_dict = self._get_uploud_link(disk_file_path=disk_file_path)
        href = link_dict.get('href', '')
        response = requests.put(href, data = open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен!')

if __name__ == '__main__':
    
    disk_file_path = 'netology/Python\hw_request_http\hw_http.txt'
    filename = 'D:\Python\hw_request_http\hw_http.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(disk_file_path, filename)
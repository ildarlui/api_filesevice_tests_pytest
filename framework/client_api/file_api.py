import requests

BASE_API_URL = 'URL'


class APIFile:

    def add_file_fileservice(self, file):
        url = f"{BASE_API_URL}/api/files"
        response = requests.request("POST", url, files=file)
        return response.json()

    def update_expiration_date_file_fileservice(self, fileId, payload):
        url = f"{BASE_API_URL}/api/files/{fileId}/"
        headers = {'Content-Type': 'application/json'}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        return response

    def delete_file_fileservice(self, fileId):
        url = f"{BASE_API_URL}/api/files/{fileId}"
        response = requests.request("DELETE", url)
        return response

    def get_file_fileservice(self, fileIdId):
        url = f'{BASE_API_URL}/api/files/{fileIdId}'
        response = requests.get(url)
        return response.json()

    def get_url_downloads_file_fileservice(self, fileId):
        url = f"{BASE_API_URL}/api/files/{fileId}/urls"
        response = requests.request("GET", url)
        return response.json()

    def get_downloads_file_fileservice(self, fileId):
        url = f"{BASE_API_URL}/api/files/{fileId}/downloads"
        response = requests.request("GET", url)
        return response

    def delete_expired_files_from_fileservice(self):
        url = f"{BASE_API_URL}/api/files/expired"
        response = requests.request("DELETE", url)
        return response

    def downloads_nginx(self, data):
        url = f"http://172.21.28.6:9000{data}"
        response = requests.request("GET", url)
        return response
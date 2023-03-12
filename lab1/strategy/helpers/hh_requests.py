import requests


__all__ = [
    "HHRequests"
]


class HHRequests:
    def __init__(self, base_url: str, headers: dict) -> None:
        self.headers = headers
        self.base_url = base_url

    def set_base_url(self, new_base_url: str) -> None:
        self.base_url = new_base_url

    def set_headers(self, new_headers: str) -> None:
        self.headers = new_headers

    def get(self, path: str, params: dict = None) -> requests.Response:
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        r = requests.get(url, params=params, headers=self.headers)
        return r

    def post(self, path: str, body: dict) -> requests.Response:
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        r = requests.post(url, headers=self.headers, json=body)
        return r

    def put(self, path: str, body: dict) -> requests.Response:
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        r = requests.put(url, headers=self.headers, json=body)
        return r

    def delete(self, path: str) -> requests.Response:
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        r = requests.put(url, headers=self.headers)
        return r

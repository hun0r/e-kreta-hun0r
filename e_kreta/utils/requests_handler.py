import requests

class RequestsHandler:
    @staticmethod
    def get(url, headers, params=None, proxies=None):
        response = requests.get(url, headers=headers, params=params, proxies=proxies)
        response.raise_for_status()
        return response

    @staticmethod
    def post(url, headers, data=None, proxies=None):
        response = requests.post(url, headers=headers, data=data, proxies=proxies)
        response.raise_for_status()
        return response

    @staticmethod
    def delete(url, headers, proxies=None):
        response = requests.delete(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        return response

"""helpers methods common fpr application"""
# import urllib.request
import json

# import requests
# from requests.exceptions import HTTPError
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import socket


def get_json_from_url(source: str):
    """load data from source url and tramsform it to json format"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Safari/537.36 YaBrowser/22.9.3.888 Yowser/2.5 Edge/18.19582"
    }
    request = Request(source, headers=headers or {})
    try:
        # with urlopen(source, timeout=100) as url:
        with urlopen(request, timeout=100) as response:
            # print(response.status)
            result = json.load(response)
            return result
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}, {http_err.status}, {http_err.code}")
    except URLError as url_error:
        if isinstance(url_error.reason, socket.timeout):
            # logging.error('socket timed out - URL %s', url)
            print(f"socket timed out - URL {url_error}")
            raise URLError(url_error.reason)
        else:
            print("some other error happened - URL {url_error}")
            raise URLError(url_error.reason)
    except Exception as err:
        print(f"Other error occurred: {err}")
        exit()

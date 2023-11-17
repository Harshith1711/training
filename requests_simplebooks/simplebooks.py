import requests
import json
from urllib.parse import urljoin
from data import cred


baseurl = "https://simple-books-api.glitch.me/"
token = None  # Initialize token
orderId = None  # Initialize orderId

class RestAPIMethods:
    def token(self, url=None, body=None, headers=None, auth=None):
        global token
        endpoint = baseurl + url

        credentials = cred()
        response = requests.post(urljoin(baseurl, endpoint), json=credentials)

        res = response.json()['accessToken']
        token = res
        return res

    def get_req(self, url=None, body=None, headers=None, auth=None):
        endpoint = baseurl + url
        headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
        get_request = requests.get(endpoint, json=body, headers=headers)
        print("GET request status code:", get_request.status_code)

        return get_request

    def post_req(self, url=None, body=None, headers=None, auth=None):
        global orderId
        endpoint = baseurl + url
        headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
        post_request = requests.post(endpoint, json=body, headers=headers)
        print("POST request status code:", post_request.status_code)
        orderId = post_request.json().get('orderId')

        return post_request

    def update_req(self, url=None, body=None, headers=None, auth=None):
        endpoint = baseurl + url
        headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
        patch_request = requests.patch(endpoint, json=body, headers=headers)

        try:
            # Check if the response has content before trying to parse it as JSON
            response_json = patch_request.json()
            print("PATCH request test:", response_json)
        except json.decoder.JSONDecodeError:
            print("PATCH request has no JSON content")

        print("PATCH request status code:", patch_request.status_code)

        return patch_request

    def delete_req(self, url=None, body=None, headers=None, auth=None):
        endpoint = baseurl + url
        headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
        delete_request = requests.get(endpoint, json=body, headers=headers)
        print("delete request status code:", delete_request.status_code)

        return  delete_request



import requests


class BaiduAuth:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_access_token(self):
        url = "https://aip.baidubce.com/oauth/2.0/token"
        param = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.post(url, param, headers=headers)
        M = response.json()
        W = M.get("access_token")
        return W

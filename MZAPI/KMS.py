import requests


class KMS:
    def __init__(self):
        pass

    def kms(self, W):
        """
        从指定的URL获取数据。
        参数:
        W (str): 要获取的数据的键名。
        返回:
        str: 获取的数据值，如果未找到则返回"not found"。
        """
        # 目标URL
        url = "https://img.blog.mizhoubaobei.top/1.json"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                M = response.json()
                data = M.get(W, "not found")
                return data
            else:
                return f"Failed to retrieve data, status code: {response.status_code}"
        except requests.RequestException as e:
            return f"An error occurred: {e}"

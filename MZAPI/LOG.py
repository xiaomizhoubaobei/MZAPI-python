from threading import Thread

import requests


class PublicIPTracker:
    def __init__(self):
        """ """
        self.public_ip = None
        self.ip_details = None

    def get_public_ip(self):
        """获取公网IP地址"""
        try:
            response = requests.get("https://httpbin.org/ip")
            self.public_ip = response.json()["origin"]
            return self.public_ip
        except requests.RequestException as e:
            print(f"获取公网IP失败: {e}")
            return None

    def get_public_ip_details(self):
        """获取公网IP的详细信息"""
        if self.public_ip is None:
            self.get_public_ip()
        try:
            url = (
                f"https://qifu-api.baidubce.com/ip/geo/v1/district?ip={self.public_ip}"
            )
            response = requests.get(url)
            self.ip_details = response.json()
            return self.ip_details
        except requests.RequestException as e:
            print(f"获取公网IP详细信息失败: {e}")
            return None

    def track_log(self):
        """将日志发送到指定的URL"""
        if self.ip_details is None:
            self.get_public_ip_details()
        return self.ip_details

    def start_track_log(self):
        # 使用线程来处理日志
        thread = Thread(target=self.track_log)
        thread.start()

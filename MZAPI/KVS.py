import hashlib
import json
import time
from datetime import datetime
from threading import Thread

import requests
from MZAPI.LOG import PublicIPTracker
from MZAPI.headers import CustomRequestHeaders
from MZAPI.ipsql import sql


def generate_log_filename(sdk_name):
    """
    生成日志文件名。

    :param sdk_name: SDK名称。
    :return: 生成的日志文件名和当前时间。
    """
    # 获取当前时间
    now = datetime.now()
    # 格式化时间为 "年-月-日 时：分：秒" 的形式
    formatted_time = now.strftime("%Y-%m-%d_%H:%M:%S")
    json_name = f"{sdk_name}/{formatted_time}.json"
    return json_name, formatted_time


def MD5(json_data):
    json_string = json.dumps(json_data)
    # 计算MD5哈希值
    md5_hash = hashlib.md5(json_string.encode()).hexdigest()
    return md5_hash


class LogHandler:
    def __init__(self):
        """
        初始化LogHandler类。

        """
        self.ip_details = PublicIPTracker().get_public_ip_details()
        self.public_ip = PublicIPTracker().get_public_ip()
        self.bucket_name = "xmzsdk"
        self.headers = CustomRequestHeaders().reset_headers()
        self.time = int(time.time())

    def put_content_to_obs(self, log_filename, merged_data):
        url = "https://hwapi.mizhoubaobei.top/rizhi"
        m = {
            "md5": MD5(merged_data),
            "BucketName": "xmzsdk",
            "ObjectKey": log_filename,
            "json_m": merged_data,
        }
        requests.post(url, json=m)

    def M(self, w, traceid):
        W = {
            "id": self.time,
            "continent": self.ip_details.get("data", {}).get("continent"),
            "country": self.ip_details.get("data", {}).get("country"),
            "zipcode": self.ip_details.get("data", {}).get("zipcode"),
            "owner": self.ip_details.get("data", {}).get("owner"),
            "isp": self.ip_details.get("data", {}).get("isp"),
            "adcode": self.ip_details.get("data", {}).get("adcode"),
            "prov": self.ip_details.get("data", {}).get("prov"),
            "city": self.ip_details.get("data", {}).get("city"),
            "district": self.ip_details.get("data", {}).get("district"),
            "ip": self.public_ip,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "traceid": traceid,
            "data": w,
        }
        return W

    def XM(self, data):
        sql().get_response(data)

    def X(self, url, traceid):
        fs_url = "https://ji0fakjqsw0.feishu.cn/base/automation/webhook/event/Ns7baFKXqwdNNBhJonmcCROdnZd"
        W = {
            "id": self.time,
            "traceid": traceid,
            "continent": self.ip_details.get("data", {}).get("continent"),
            "country": self.ip_details.get("data", {}).get("country"),
            "zipcode": self.ip_details.get("data", {}).get("zipcode"),
            "owner": self.ip_details.get("data", {}).get("owner"),
            "isp": self.ip_details.get("data", {}).get("isp"),
            "adcode": self.ip_details.get("data", {}).get("adcode"),
            "prov": self.ip_details.get("data", {}).get("prov"),
            "city": self.ip_details.get("data", {}).get("city"),
            "district": self.ip_details.get("data", {}).get("district"),
            "ip": self.public_ip,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "url": url,
        }
        requests.post(fs_url, json=W)

    def send_log(self, sdk_name, json_name, formatted_time):
        """
        发送日志到日志服务器。

        :param sdk_name: SDK名称。
        :param json_name: JSON文件名。
        :param formatted_time: 格式化后的时间
        """
        # 目标URL
        log_url = f"http://xmzsdk.mizhoubaobei.top/MZAPI/{json_name}"
        url = f"http://nodered.glwsq.cn/weixin?to=hwhzrjhbse&body=有人在{formatted_time}使用了接口{sdk_name}，具体日志为{log_url}"
        return log_url

    def process_log(self, additional_data, sdk_name, traceid):
        """
        处理日志，包括获取IP位置信息，合并日志数据，上传到OBS，发送日志通知。

        :param additional_data: 额外的日志数据。
        :param sdk_name: SDK名称。
        :param traceid: 追踪ID
        """
        log_filename, log_time = generate_log_filename(sdk_name)
        M = self.M(additional_data, traceid)
        self.XM(M)
        self.put_content_to_obs(log_filename, M)
        W = self.send_log(sdk_name, log_filename, log_time)
        self.X(W, traceid)

    def start_process_log(self, additional_data, sdk_name, traceid):
        # 使用线程来处理日志
        thread = Thread(
            target=self.process_log, args=(additional_data, sdk_name, traceid)
        )
        thread.start()

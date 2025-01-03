import requests
from MZAPI.headers import CustomRequestHeaders


class sql:
    def __init__(self):
        # 初始化sql类，创建一个CustomRequestHeaders实例
        self.headers = CustomRequestHeaders()

    def get_response(self, uuid, question, answer, trace_id, ip, api_name):
        """
        发送包含uuid、question和answer的POST请求到指定URL。

        参数:
        uuid (str): 用户的唯一标识符
        question (str): 用户的问题
        answer (str): 系统的回答
        trace_id (str): 跟踪ID
        ip (str): 用户的IP地址
        api_name (str): API的名称

        返回:
        None
        """
        url = "https://hwapi.mizhoubaobei.top/sql"

        headers = self.headers.reset_headers()
        body = {
            "uuid": uuid,
            "question": question,
            "answer": answer,
            "trace_id": trace_id,
            "ip": ip,
            "api_name": api_name
        }
        requests.post(url, headers=headers, json=body)

import datetime
import json
import time
import uuid

import requests
from MZAPI.APM import APMClient
from MZAPI.KVS import LogHandler
from MZAPI.LOG import PublicIPTracker
from MZAPI.MB import baiduauth
from MZAPI.headers import CustomRequestHeaders
from MZAPI.sql import sql
from opentelemetry import trace


class EightK:
    """
    EightK 类用于与百度ERNIE 4.0 8K模型进行交互。

    初始化参数:
    :param client_name: 客户端名称
    :param ak: 百度API的访问密钥
    :param sk: 百度API的安全密钥

    主要方法:
    - get_response: 发送请求到ERNIE 4.0 8K模型并获取响应
    """

    def __init__(self, client_name, ak, sk):
        self.ip = PublicIPTracker().get_public_ip()
        self.ak = ak
        self.sk = sk
        self.access_token = baiduauth.BaiduAuth(ak, sk)
        self.log = LogHandler()
        self.headers = CustomRequestHeaders().reset_headers()
        self.sql = sql()
        self.apm_client = APMClient(
            client_name=client_name,
            host_name="ERNIE-4.0-8K",
            token="kCrxvCIYEzhZfAHETXEB",
            peer_service="ERNIE-4.0-8K",
            peer_instance=" 180.97.107.95:443",
            peer_address=" 180.97.107.95",
            peer_ipv6="240e:ff:e020:934:0:ff:b0dc:3636",
            http_host="https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro",
            server_name="MZAPI",
        )
        self.tracer = self.apm_client.get_tracer()

    def get_response(
        self,
        data,
        temperature=None,
        top_p=None,
        penalty_score=None,
        enable_system_memory=None,
        disable_search=None,
        enable_citation=None,
        stream=None,
        system=None,
        stop=None,
        enable_trace=None,
        max_output_tokens=None,
    ):
        """
        发送请求到ERNIE 4.0 8K模型并获取响应。

        :param data: 用户输入的数据 (必填)
        :param temperature: 控制生成文本的随机性 (选填)
        :param top_p: 控制生成文本的多样性 (选填)
        :param penalty_score: 惩罚分数，用于控制生成文本的重复性 (选填)
        :param enable_system_memory: 是否启用系统记忆 (选填)
        :param disable_search: 是否禁用搜索 (选填)
        :param enable_citation: 是否启用引用 (选填)
        :param stream: 是否启用流式传输 (选填)
        :param system: 系统信息 (选填)
        :param stop: 停止生成的条件 (选填)
        :param enable_trace: 是否返回搜索溯源信息 (选填)
        :param max_output_tokens: 最大输出tokes数 (选填)
        :return: 包含响应数据的字典

        """
        with self.tracer.start_as_current_span("ERNIE-4.0-8K") as span:
            access_token = self.access_token.get_access_token()
            url = (
                "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token="
                + access_token
            )
            payload = json.dumps(
                {
                    "messages": [{"role": "user", "content": data}],
                    "temperature": temperature,
                    "top_p": top_p,
                    "penalty_score": penalty_score,
                    "stream": stream,
                    "enable_system_memory": enable_system_memory,
                    "system": system,
                    "stop": stop,
                    "disable_search": disable_search,
                    "enable_citation": enable_citation,
                    "enable_trace": enable_trace,
                    "max_output_tokens": max_output_tokens,
                    "response_format": "json",
                    "user_ip": self.ip,
                }
            )
            Request_id = str(uuid.uuid4())
            headers = {
                **self.headers,
                "Content-Type": "application/json",
                "Request_id": Request_id,
            }
            response = requests.post(url, headers=headers, data=payload)
            current_timestamp = int(time.time())
            dt_object = datetime.datetime.fromtimestamp(current_timestamp)
            formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")
            X = json.loads(payload)
            span.set_attribute("HTTP_method", "POST")
            span.set_attribute("HTTP_url", url)
            span.set_attribute("Request_id", headers.get("Request_id"))
            if X.get("temperature") is not None:
                span.set_attribute("temperature", X.get("temperature"))
            if X.get("top_p") is not None:
                span.set_attribute("top_p", X.get("top_p"))
            if X.get("penalty_score") is not None:
                span.set_attribute("penalty_score", X.get("penalty_score"))
            if X.get("stream") is not None:
                span.set_attribute("stream", X.get("stream"))
            if X.get("enable_system_memory") is not None:
                span.set_attribute(
                    "enable_system_memory", X.get("enable_system_memory")
                )
            if X.get("system") is not None:
                span.set_attribute("system", X.get("system"))
            if X.get("stop") is not None:
                span.set_attribute("stop", X.get("stop"))
            if X.get("disable_search") is not None:
                span.set_attribute("disable_search", X.get("disable_search"))
            if X.get("enable_citation") is not None:
                span.set_attribute("enable_citation", X.get("enable_citation"))
            if X.get("enable_trace") is not None:
                span.set_attribute("enable_trace", X.get("enable_trace"))
            if X.get("max_output_tokens") is not None:
                span.set_attribute("max_output_tokens", X.get("max_output_tokens"))
            span.set_attribute("user_ip", X.get("user_ip"))
            span.set_attribute("HTTP_status_code", response.status_code)
            span.set_attribute("HTTP_response_content", response.content)
            span.set_attribute("HTTP_response_size", len(response.content))
            span.set_attribute(
                "http.response_time", response.elapsed.total_seconds() * 1000
            )
            span.set_attribute("question", data)
            span.set_attribute("API_key", self.ak)
            span.set_attribute("secret_key", self.sk)
            span.set_attribute("access_token", access_token)
            current_span = trace.get_current_span()
            traceID = current_span.get_span_context().trace_id
            W = trace.span.format_trace_id(traceID)
            self.log.start_process_log(response.json(), "ERNIE-4.0-8K", W)
            M = response.json()
            uuid1 = Request_id
            question = data
            answer = M.get("result")
            X = {
                "id": current_timestamp,
                "traceID": W,
                "time": formatted_time,
                "response": M,
            }
            self.sql.get_response(uuid1, question, answer, W, self.ip, "ERNIE-4.0-8K")
            return X

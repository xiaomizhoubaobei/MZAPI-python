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
from MZAPI.sql import SqlRequest
from MZAPI.KMS import KMS
from opentelemetry import trace


class BaseERNIEModel:
    """
    BaseERNIEModel 类用于与百度ERNIE模型进行交互。

    初始化参数:
    :param client_name: 客户端名称
    :param ak: 百度API的访问密钥
    :param sk: 百度API的安全密钥
    :param host_name: 模型的主机名
    :param host_url: 模型的主机URL

    主要方法:
    - get_response: 发送请求到ERNIE-Novel-8K
    """

    def __init__(self, client_name, ak, sk, host_name, host_url, token):
        """
        初始化方法。

        :param client_name: 客户端名称
        :param ak: 百度API的访问密钥
        :param sk: 百度API的安全密钥
        :param host_name: 模型名称
        :param host_url: 模型的主机URL
        """
        self.host_name = host_name
        self.host_url = host_url
        self.ip = PublicIPTracker().get_public_ip()
        self.ak = ak
        self.sk = sk
        self.access_token = baiduauth.BaiduAuth(ak, sk)
        self.log = LogHandler()
        self.headers = CustomRequestHeaders().reset_headers()
        self.sql = SqlRequest()
        if token is None:
            token =  KMS().kms("APMtoken")
        self.apm_client = APMClient(
            client_name=client_name,
            host_name=self.host_name,
            token=token,
            peer_service=self.host_name,
            peer_instance=" 180.97.107.95:443",
            peer_address=" 180.97.107.95",
            peer_ipv6="240e:ff:e020:934:0:ff:b0dc:3636",
            http_host=self.host_url,
            server_name="MZAPI",
        )
        self.tracer = self.apm_client.get_tracer()
        self.access_token = self.access_token.get_access_token()

    def get_response(
            self,
            data,
            temperature,
            top_p,
            penalty_score,
            enable_system_memory,
            disable_search,
            enable_citation,
            stream,
            system,
            stop,
            enable_trace,
            max_output_tokens,
    ):
        with self.tracer.start_as_current_span(self.host_name) as span:
            url = f"{self.host_url}?access_token={self.access_token}"
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
            response = requests.post(url, headers=headers, data=payload, timeout=60)
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
            span.set_attribute("access_token", self.access_token)
            current_span = trace.get_current_span()
            traceID = current_span.get_span_context().trace_id
            W = trace.span.format_trace_id(traceID)
            self.log.start_process_log(response.json(), self.host_name, W)
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
            self.sql.get_response(uuid1, question, answer, W, self.ip, self.host_name)
            return X

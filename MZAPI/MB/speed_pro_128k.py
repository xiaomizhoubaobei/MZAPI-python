"""
ERNIE Speed Pro 128K 模型交互模块
提供与百度ERNIE大模型API对接的功能
"""

from typing import Optional, Dict, Any
from MZAPI.MB.base_ernie_model import BaseERNIEModel


class Speed_Pro_128K:
    """EightK 类用于与百度ERNIE 4.0 8K模型进行交互。

    初始化参数:
        client_name (str): 客户端名称
        ak (str): 百度API的访问密钥
        sk (str): 百度API的安全密钥
        token (str, optional): 访问令牌
    """

    def __init__(
        self,
        client_name: str,
        ak: str,
        sk: str,
        token: Optional[str] = None
    ) -> None:
        host_name = "ERNIE-Speed-Pro-128K"
        http_host = (
            "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/"
            "wenxinworkshop/chat/ernie-speed-pro-128k"
        )
        self.M = BaseERNIEModel(client_name, ak, sk, host_name, http_host, token)

    def get_response(  # pylint: disable=too-many-arguments
        self,
        data: str,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        penalty_score: Optional[float] = None,
        enable_system_memory: Optional[bool] = None,
        disable_search: Optional[bool] = None,
        enable_citation: Optional[bool] = None,
        stream: Optional[bool] = None,
        system: Optional[str] = None,
        stop: Optional[str] = None,
        enable_trace: Optional[bool] = None,
        max_output_tokens: Optional[int] = None,
    ) -> Dict[str, Any]:
        """发送请求到ERNIE模型并获取响应。

        Args:
            data (str): 用户输入数据
            temperature (float, optional): 控制生成随机性
            # 其他参数保持类似格式...

        Returns:
            Dict[str, Any]: 包含响应数据的字典
        """
        return self.M.get_response(
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
        )

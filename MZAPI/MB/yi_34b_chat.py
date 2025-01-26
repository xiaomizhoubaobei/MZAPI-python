from MZAPI.MB.base_ernie_model import BaseERNIEModel


class Yi34BChat:
    """Yi34BChat 大模型交互封装类

    初始化参数:
    :param client_name: 客户端名称
    :param ak: 百度API访问密钥
    :param sk: 百度API安全密钥
    :param token: APM令牌（可选）

    主要方法:
    - get_response: 发送请求到Yi-34B-Chat模型并获取响应
    """

    def __init__(self, client_name, ak, sk, token=None):
        host_name = "Yi-34B-Chat"
        http_host = (
            "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/yi_34b_chat"  # noqa
        )
        self.model = BaseERNIEModel(client_name, ak, sk, host_name, http_host, token)

    def get_response(  # pylint: disable=too-many-arguments
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
        """发送请求到Yi-34B-Chat模型并获取响应

        :param data: 用户输入数据（必填）
        :param temperature: 控制生成随机性（0-1，默认0.95）
        :param top_p: 核心采样概率（0-1，默认0.8）
        :param penalty_score: 重复惩罚系数（1-2，默认1.0）
        :param enable_system_memory: 启用系统记忆（默认False）
        :param disable_search: 禁用搜索功能（默认False）
        :param enable_citation: 启用引用标注（默认False）
        :param stream: 流式传输模式（默认False）
        :param system: 系统级提示词（可选）
        :param stop: 停止生成序列（可选）
        :param enable_trace: 返回搜索溯源信息（默认False）
        :param max_output_tokens: 最大输出token数（默认1024）
        :return: 包含响应数据的字典
        """
        return self.model.get_response(
            data=data,
            temperature=temperature,
            top_p=top_p,
            penalty_score=penalty_score,
            enable_system_memory=enable_system_memory,
            disable_search=disable_search,
            enable_citation=enable_citation,
            stream=stream,
            system=system,
            stop=stop,
            enable_trace=enable_trace,
            max_output_tokens=max_output_tokens,
        )

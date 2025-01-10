from MZAPI.MB.base_ernie_model import BaseERNIEModel


class EightK:
    """
    EightK 类用于与百度ERNIE 3.5 8K模型进行交互。

    初始化参数:
    :param client_name: 客户端名称
    :param ak: 百度API的访问密钥
    :param sk: 百度API的安全密钥

    主要方法:
    - get_response: 发送请求到ERNIE 3.5 8K模型并获取响应
    """

    def __init__(self, client_name, ak, sk, token=None):
            host_name="ERNIE-3.5-8K"
            http_host="https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions"
            self.M = BaseERNIEModel(client_name, host_name, http_host, ak, sk, token)

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
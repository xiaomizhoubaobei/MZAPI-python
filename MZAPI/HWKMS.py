# coding: utf-8
import random

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkkms.v2 import *
from huaweicloudsdkkms.v2.region.kms_region import KmsRegion


class HuaweiKMSEncryptor:
    """
    HuaweiKMSEncryptor 类用于与华为云KMS服务进行交互，提供数据加密功能。

    初始化参数:
    :param region: 区域，默认为 "cn-east-3"

    主要方法:
    - encrypt_data: 加密数据
    """

    def __init__(self, region="cn-east-3"):
        """
        初始化 HuaweiKMSEncryptor 类。

        :param region: 区域，默认为 "cn-east-3"
        """
        self.ak = "CHRZSAE9JCAZCZRVQNNT"
        self.sk = "Q2lFSm4QAxUiWtQHEIK0bTU5jURc8dvi27rVHv1u"
        self.region = region
        self.client = self._create_kms_client()

    def _create_kms_client(self):
        """
        创建 KMS 客户端实例。

        :return: KMS 客户端实例
        """
        credentials = BasicCredentials(self.ak, self.sk)
        return (
            KmsClient.new_builder()
            .with_credentials(credentials)
            .with_region(KmsRegion.value_of(self.region))
            .build()
        )

    @staticmethod
    def random_choice():
        """
        随机选择一个密钥 ID。

        :return: 选择的密钥 ID
        """
        options = [
            "0704c552-bc9d-4a93-aa3c-ae41eab597d9",
            "f4258649-a384-407d-9d8c-15e785953f45",
            "63cc31da-7183-4e50-88b9-3cf7cb7e459c",
            "7f8f341c-ba05-4b38-9d0b-1a4bca3a71fa",
        ]
        return random.choice(options)

    def encrypt_data(self, plain_text):
        """
        加密数据。

        :param plain_text: 明文
        :return: 加密后的响应信息
        """
        try:
            request = EncryptDataRequest()
            request.body = EncryptDataRequestBody(
                encryption_algorithm="SYMMETRIC_DEFAULT",
                plain_text=plain_text,
                key_id=self.random_choice(),
            )
            response = self.client.encrypt_data(request)
            return {"key_id": response.key_id, "cipher_text": response.cipher_text}
        except exceptions.ClientRequestException as e:
            print(f"Status Code: {e.status_code}")
            print(f"Request ID: {e.request_id}")
            print(f"Error Code: {e.error_code}")
            print(f"Error Message: {e.error_msg}")
            raise

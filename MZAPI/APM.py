from MZAPI.LOG import PublicIPTracker
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter as OTLPSpanGrpcExporter,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import SpanKind


class APMClient:
    """
    APMClient 类用于初始化和管理 OpenTelemetry 追踪。
    """

    def __init__(
        self,
        client_name,
        host_name,
        token,
        peer_service,
        peer_instance,
        peer_address,
        peer_ipv6,
        http_host,
        server_name,
        endpoint="http://ap-shanghai.apm.tencentcs.com:4317",
    ):
        """
        初始化 APM 客户端。

        :param client_name: 客户端名称。
        :param host_name: 主机名称。
        :param token: 访问令牌。
        :param peer_service: 对等服务名称。
        :param peer_instance: 对等服务实例。
        :param peer_address: 对等服务IP地址。
        :param peer_ipv6: 对等服务IPv6地址。
        :param http_host: HTTP 主机。
        :param server_name: 服务名称。
        :param endpoint: OTLP 导出器的端点。
        """
        self.ip = PublicIPTracker()
        self.service_name = server_name
        self.http_host = http_host
        self.peer_ipv6 = peer_ipv6
        self.peer_address = peer_address
        self.client_name = client_name
        self.host_name = host_name
        self.token = token
        self.endpoint = endpoint
        self.peer_service = peer_service
        self.peer_instance = peer_instance
        self.init_opentelemetry()
        self.tracer = trace.get_tracer(__name__)

    def init_opentelemetry(self):
        """
        初始化 OpenTelemetry 追踪提供者和资源属性。
        """
        resource = Resource(
            attributes={
                "host.name": self.host_name,
                "token": self.token,
                "span.kind": "SPAN_KIND_CLIENT",
                "http.client_ip": self.ip.get_public_ip(),
                "Annotation": "cs",
                "http.client.name": self.client_name,
                "telemetry.sdk.name": "米粥SDK",
                "telemetry.sdk.version": "1.0.0",
                "component": "http",
                "peer.service": self.peer_service,
                "peer.instance": self.peer_instance,
                "peer.address": self.peer_address,
                "peer.ipv4": self.peer_address,
                "peer.ipv6": self.peer_ipv6,
                "peer.port": "443",
                "http.host": self.http_host,
                "service.name": self.service_name,
            }
        )
        span_processor = BatchSpanProcessor(
            OTLPSpanGrpcExporter(endpoint=self.endpoint)
        )
        tracer_provider = TracerProvider(
            resource=resource, active_span_processor=span_processor
        )
        trace.set_tracer_provider(tracer_provider)

    def start_span(self, name, kind=SpanKind.CLIENT):
        """
        启动一个新的跟踪跨度。

        :param name: 跨度名称。
        :param kind: 跨度类型，默认为 SpanKind.CLIENT。
        :return: 跟踪跨度对象。
        """
        return self.tracer.start_as_current_span(name, kind=kind)

    def set_span_attributes(self, span, attributes):
        """
        设置跟踪跨度的属性。

        :param span: 跟踪跨度对象。
        :param attributes: 属性字典。
        """
        for key, value in attributes.items():
            span.set_attribute(key, value)

    def get_tracer(self):
        """
        获取 Tracer 实例。

        :return: Tracer 实例。
        """
        return self.tracer

    def get_current_trace_id(self):
        """
        获取当前跟踪 ID。

        :return: 跟踪 ID。
        """
        current_span = trace.get_current_span()
        traceID = current_span.get_span_context().trace_id
        print("int traceID:", traceID)
        W = trace.span.format_trace_id(traceID)
        return W

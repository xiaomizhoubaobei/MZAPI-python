from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="MZAPI",
    version="0.3.4",
    description="米粥SDK",
    license_expressions=["MIT"],
    packages=find_packages(),
    install_requires=[
        # 这里添加你的包依赖，例如：
        "opentelemetry-api",
        "opentelemetry-sdk",
        "opentelemetry-exporter-otlp",
        "requests",
        "aiohttp",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="小米粥",
    author_email="mzapi@x.mizhoubaobei.top",
    url="https://github.com/xiaomizhoubaobei/XMZSDK-python",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    Verified_details ={
        "Homepage": "https://github.com/xiaomizhoubaobei/XMZSDK-python",
        "Download": "https://github.com/xiaomizhoubaobei/XMZSDK-python/releases",
        "Issues": "https://github.com/xiaomizhoubaobei/XMZSDK-python/issues",
        "Bug": "https://github.com/xiaomizhoubaobei/XMZSDK-python/issues",
        "GitHub": "https://github.com/xiaomizhoubaobei/XMZSDK-python",
        "Twitter": "https://x.com/XinXiao12088",
        "Pypi": "https://pypi.org/project/MZAPI/"
    }
)

# MZAPI 问题排查指南

在使用`MZAPI`时，你可能会遇到一些问题。以下是一些常见问题的解决方法：

## 安装问题

**问题**：无法安装 `MZAPI`。

**可能的原因**：
- 网络连接问题。
- `pip` 版本过旧。
- 包名拼写错误。
- Python 版本不兼容。
- 权限问题（在尝试安装全局包时）。

**解决方法**：
1. **检查网络连接**：
   - 确保你的设备已连接到互联网，并且没有任何网络限制（如防火墙或代理）阻止访问 PyPI。

2. **升级 `pip`**：
   - 使用以下命令升级到最新版本的 `pip`：
     ```bash
     pip install --upgrade pip
     ```

3. **使用正确的命令安装 `MZAPI`**：
   - 确保你使用的是正确的命令来安装 `MZAPI`：
     ```bash
     pip install MZAPI
     ```
   - 请注意，包名是区分大小写的。

4. **检查 Python 版本**：
   - 确保你的 Python 版本与 `MZAPI` 兼容。你可以通过以下命令检查 Python 版本：
     ```bash
     python --version
     ```
     或者：
     ```bash
     python3 --version
     ```
   - 如果需要，升级到支持的 Python 版本。

5. **查看错误日志**：
   - 如果安装失败，仔细查看错误日志。错误信息通常会提供关于问题的详细信息。

6. **使用国内镜像源**（如网络访问PyPI较慢或不稳定）：
   - 可以尝试使用国内的镜像源来加速下载，以下是几个常用的国内`pip`源及其使用方法。

## 国内常用 pip 源列表

在使用 `pip` 安装 Python 包时，由于网络原因，有时会遇到下载速度慢或连接超时的问题。为了解决这个问题，可以使用国内的镜像源来加速下载。

### 1. 阿里云开源镜像站

- **URL**：`https://mirrors.aliyun.com/pypi/simple/`

- **使用方法**：
  - **临时使用**：
    ```bash
    pip install MZAPI -i https://mirrors.aliyun.com/pypi/simple/
    ```
  - **永久配置**：
    - 在 Linux 或 macOS 上，编辑 `~/.pip/pip.conf` 文件；
    - 在 Windows 上，编辑 `%APPDATA%\pip\pip.ini` 文件。
    - 添加以下内容：
      ```ini
      [global]
      index-url = https://mirrors.aliyun.com/pypi/simple/
      ```

### 2. 华为云开源镜像站

- **URL**：`https://mirrors.huaweicloud.com/pypi/simple/`

- **使用方法**：
  - **临时使用**：
    ```bash
    pip install MZAPI -i https://mirrors.huaweicloud.com/pypi/simple/
    ```
  - **永久配置**：
    - 在 Linux 或 macOS 上，编辑 `~/.pip/pip.conf` 文件；
    - 在 Windows 上，编辑 `%APPDATA%\pip\pip.ini` 文件。
    - 添加以下内容：
      ```ini
      [global]
      index-url = https://mirrors.huaweicloud.com/pypi/simple/
      ```

### 3. 豆瓣开源镜像站

- **URL**：`https://pypi.douban.com/simple/`

- **使用方法**：
  - **临时使用**：
    ```bash
    pip install MZAPI -i https://pypi.douban.com/simple/
    ```
  - **永久配置**：
    - 在 Linux 或 macOS 上，编辑 `~/.pip/pip.conf` 文件；
    - 在 Windows 上，编辑 `%APPDATA%\pip\pip.ini` 文件。
    - 添加以下内容：
      ```ini
      [global]
      index-url = https://pypi.douban.com/simple/
      ```

### 4. 中国科学技术大学开源软件镜像站

- **URL**：`https://pypi.mirrors.ustc.edu.cn/simple/`

- **使用方法**：
  - **临时使用**：
    ```bash
    pip install MZAPI -i https://pypi.mirrors.ustc.edu.cn/simple/
    ```
  - **永久配置**：
    - 在 Linux 或 macOS 上，编辑 `~/.pip/pip.conf` 文件；
    - 在 Windows 上，编辑 `%APPDATA%\pip\pip.ini` 文件。
    - 添加以下内容：
      ```ini
      [global]
      index-url = https://pypi.mirrors.ustc.edu.cn/simple/
      ```

### 选择合适的镜像源

根据自己的网络环境和地理位置，选择一个速度较快的镜像源可以提高 `pip` 安装包的速度。如果在使用过程中遇到任何问题，可以参考相关镜像站的官方文档或联系镜像站的支持团队获取帮助。

## 网络问题

**问题**：API 调用超时或连接失败。

**解决方法**：
1. 检查你的网络连接。
2. 如果你在公司或学校网络下，可能需要配置代理。
3. 尝试增加请求超时时间。

## 日志和错误信息

**问题**：如何获取更多错误信息？

**解决方法**：
1. 使用 `try-except` 块捕获异常，并打印出错误信息。

## 其他问题

如果你遇到的问题不在上述列表中，或者上述解决方法无法解决你的问题，请通过以下方式联系我们：

- **开发者邮件**：[mzapi@x.mizhoubaobei.top](mailto:mzapi@x.mizhoubaobei.top)
- **项目网址**：[https://github.com/xiaomizhoubaobei/MZAPI-python](https://github.com/xiaomizhoubaobei/MZAPI-python)
- **注意事项**：如需帮助提供响应中的追踪ID（traceID），以便我们更好地帮助你解决问题。

我们会尽快回复你的问题，并提供进一步的帮助。

---

我们希望这个指南能帮助你解决使用 `MZAPI` 时遇到的问题。如果你有任何建议或反馈，欢迎通过 [贡献指南](CONTRIBUTING.md) 提交给我们。
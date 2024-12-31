# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置环境变量
ENV HF_HOME=/cfs/.cache/huggingface/hub


# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器中的 /app 目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序使用的端口（例如 8080）
#EXPOSE 8080

# 运行应用程序
CMD ["python", "app.py"]

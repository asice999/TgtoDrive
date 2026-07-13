# 使用Python 3.13作为基础镜像
FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 设置Python不缓冲输出
ENV PYTHONUNBUFFERED=1

# 先复制依赖清单，单独安装（利用缓存）
COPY requirements.txt .
# 安装依赖并清理pip缓存（合并到同一层减少镜像层数）
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# 再复制其他文件（代码变动不影响依赖层缓存）
COPY . /app

# 编译Python文件为.pyc，然后删除所有.py源文件
RUN python -m compileall -b . && \
    find . -name '*.py' -delete

# 运行编译后的Python脚本
CMD ["python", "-O", "tgto123.pyc"]

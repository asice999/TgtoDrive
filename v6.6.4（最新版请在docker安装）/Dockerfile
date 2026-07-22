# ============================================
# Builder: install deps, apply patches, compile
# ============================================
FROM python:3.13-slim AS builder

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# 依赖安装（变动少，单独层利用缓存）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# 合并补丁，减少层数
COPY patch_p115client.py .
RUN sed -i 's|format_header_param = fields.format_header_param|format_header_param = getattr(fields, "format_header_param", None)|' \
        /usr/local/lib/python3.13/site-packages/telebot/apihelper.py && \
    python3 patch_p115client.py && \
    rm patch_p115client.py

# 复制源码、编译、删除源文件
COPY . .
RUN python -m compileall -b . && \
    find . -name '*.py' -type f -delete && \
    find . -type d -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null; true

# ============================================
# Runtime: 只拿最终产物
# ============================================
FROM python:3.13-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# 从 builder 复制已安装的包 + 编译后的应用
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /app /app

# 清理 apt 缓存
RUN rm -rf /var/lib/apt/lists/*

CMD ["python", "-O", "tgto123.pyc"]
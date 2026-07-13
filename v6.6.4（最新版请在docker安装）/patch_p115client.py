"""Patch p115client: add multipart_upload_init alias to upload.py."""
import os, p115client.tool.upload as u

patch = """

# --- patched by TgtoDrive ---
def multipart_upload_init(client, path, filename="", filesize=-1, filesha1="", pid=0):
    return upload_init(client=client, file=path, pid=pid, filename=filename, filesha1=filesha1, filesize=filesize)
# --- end patch ---
"""

with open(u.__file__, "a") as f:
    f.write(patch)

print("Patched:", u.__file__)
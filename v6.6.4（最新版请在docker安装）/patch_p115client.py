"""Patch p115client to add multipart_upload_init compatibility alias."""
import p115client.tool.upload as u


def multipart_upload_init(client, path, filename="", filesize=-1, filesha1="", pid=0):
    """Compatibility wrapper: old multipart_upload_init -> new upload_init."""
    return u.upload_init(
        client=client, file=path, pid=pid,
        filename=filename, filesha1=filesha1, filesize=filesize,
    )


u.multipart_upload_init = multipart_upload_init
print("patched: p115client.tool.upload.multipart_upload_init -> upload_init")
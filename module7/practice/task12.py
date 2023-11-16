import base64


def encode_data_to_base64(data):
    a = []
    for el in data:
       message_bytes = el.encode("utf-8")
       base64_bytes = base64.b64encode(message_bytes)
       a.append(base64_bytes.decode('utf-8'))
    return a
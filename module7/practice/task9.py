def is_equal_string(utf8_string, utf16_string):
    return utf8_string.decode()==utf16_string.decode('utf-16')
print(is_equal_string())
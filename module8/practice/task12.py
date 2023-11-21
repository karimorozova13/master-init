def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as fh:
        fh.write(additional_info)
    with open(path, 'r') as fh2:
       fh2.seek(start_pos)
       s= fh2.read(count_chars)
    return s
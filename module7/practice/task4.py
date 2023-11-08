def add_employee_to_file(record, path):
    fh= open(path, 'a')

    fh.write(f'{record}\n')
    fh.close()
    return True
print(add_employee_to_file("new line,19",'new_list.txt'))
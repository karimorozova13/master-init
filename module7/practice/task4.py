def add_employee_to_file(record, path):
    fh= open(path, 'a')
    fh.write('\n')

    fh.write(record)
    fh.close()
    return True
print(add_employee_to_file("nfdsfdsfew gfdgdfg,19",'new_list.txt'))
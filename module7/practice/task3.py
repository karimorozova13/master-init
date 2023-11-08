def read_employees_from_file(path):
    fh= open(path, 'r')
    arr= fh.readlines()
    a =[]
    for emp in arr:
       a.append(emp.split("\n")[0])

    fh.close()
    return a
print(read_employees_from_file('new_list.txt'))
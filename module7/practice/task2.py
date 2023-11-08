def write_employees_to_file(employee_list, path):
    fh= open(path, 'w')
   
    str=''
    for dep in employee_list:
        for emp in dep:
            str+=f'{emp}\n'
  
    fh.write(str)
    
    fh.close()
    return True

print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'new_list.txt'))
def total_salary(path):
    fh = open(path, 'r')
    total = 0
    while True:
        line = fh.readline()
        if not line:
            break
        salary = line.split(',')[1]
        total +=int(salary)
        print(salary)
    fh.close()
    return float(total)

print(total_salary('emploees.txt'))
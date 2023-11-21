def get_employees_by_profession(path, profession):
    with open(path,'r') as fh:
        all_employee = fh.readlines()
        new_s = []
        for s in all_employee:
            if not s.find(profession) == -1:
                new_s.append(s.removesuffix(f'{profession}\n').strip())
    return (' ').join(new_s).strip()
print(get_employees_by_profession('emploee.txt', 'cook'))
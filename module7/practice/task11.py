def get_credentials_users(path):
    with open(path, 'rb') as fh:
        file = fh.readlines()
        s = []
        for el in file:
            str = el.decode('utf-8')
            new_str = str.split('\n')
            print(new_str)
            s.append(new_str[0])
        
        return s
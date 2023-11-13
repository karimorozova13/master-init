def get_credentials_users(path):
    with open(path, 'br') as fh:
        file = fh.read()
        s = file.decode('utf-8')
        print(s)
        # for el in file:
        #     print(el[1::].decode('utf-8'))
        # print(file)
        return True
print(get_credentials_users('univer.bin'))
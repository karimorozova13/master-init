data = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

def save_credentials_users(path, users_info):
    
    with open(path, 'wb') as fh:
        for key,val in users_info.items():
            print(key,val)
            str = f'{key}:{val}\n'
            fh.write(str.encode('utf-8'))
save_credentials_users('univer.txt',data)
# __repr__ -> return class with arg self

class Adder:
    def __init__(self,add_val):
        self.add_val= add_val
    def __call__(self,val):
        return self.add_val + val
a2 = Adder(2)
print(a2(10))

class Session:
    def __init__(self,addr, port=3000):
        self.connected = True
        self.addr= addr
        self.port = port
    def __enter__(self):
        print(f'Connected to {self.addr}:{self.port}')
        return self
    def __exit__(self, exception_type,exception_value, traceback):
        self.connected= False
        if exception_type is not None:
            print('Something went wrong')
        else:
            print('No problem')
            
            
localhost_connection = Session('localhost')

with localhost_connection as session:
    print(localhost_connection is session)
    print(localhost_connection.connected)
    
print(localhost_connection.connected)

with Session('port', 'local') as connection:
    # raise Exception('Oh no!!!!')
    pass

    
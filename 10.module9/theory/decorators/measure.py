from time import sleep,time

def measure(fn):
    def inner(*args, **kwargs):
        t= time()
        fn(*args, **kwargs)
        print(f"{fn.__name__} took {int(time() - t)} seconds")
    return inner

@measure
def calculate_num_pi():
    sleep(10)
    
calculate_num_pi()


# parameters decorator 
def decorator(fn):
    def inner():
        def wraper():
            pass
        return wraper
    return inner

@decorator(12, 'fsdfg')
def fn():
    pass
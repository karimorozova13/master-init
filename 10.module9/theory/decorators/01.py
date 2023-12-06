from functools import wraps

def star(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print('*'*10)
        fn(*args, **kwargs)
        print('*'* 10)
    return inner

def percent(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print('%'*10)
        fn(*args, **kwargs)
        print('%'* 10)
    return inner


@percent
@star
def christmas_msg(msg):
    print(msg)

christmas_msg('Merry Christmas!')
christmas_msg.__wrapped__('Kari')
christmas_msg.__wrapped__.__wrapped__('Kari')

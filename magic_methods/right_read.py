from time import perf_counter
import resource

# generator reading
def read_field_yield(path):
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            fh.close()
            break
    yield line

# iterator reading
def read_from_file(path):
    with open(path, 'r') as fh:
        data = fh.readlines()
    return data

start =  perf_counter()

print(perf_counter() - start)
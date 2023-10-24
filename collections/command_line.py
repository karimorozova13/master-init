import sys

for arg in sys.argv:
    print(arg)

def main():
    print(sys.argv[0])
main()
def parse_args():
    result = ""
    result = ' '.join(sys.argv[1::])
    
    return result
print(parse_args())
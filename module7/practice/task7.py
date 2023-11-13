import re

def sanitize_file(source, output):
    str=''
    with open(source, 'r') as fh:
        file= fh.read()
        str = re.sub(r'\d', '', file)
        
    with open(output, 'w') as fh1:
        fh1.write(str)
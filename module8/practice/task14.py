def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh:
        lines =fh.readlines()
    with open(output_file, 'w') as fh2:
        i = 0
        for l in lines:
            fh2.write(f'{i}: {l}')
            i +=1
            
print(to_indexed('emploee.txt','new.txt'))
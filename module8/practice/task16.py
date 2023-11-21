def encode(data):
    if not data:
        return []

    x = data[0]
    count =1
    arr =[]
    
    
    for el in data[1::]:
        if el==x:
            count +=1
                
        else:
            arr.append(x)
            arr.append(count)
            arr +=encode(data[count::])
            return arr
    arr.append(x)
    arr.append(count)
            
    return arr
print(encode(['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]))

def decode(data):
    if not data:
        return []
    arr =[]
    x= data[0]
    count = 1
    idx =0
    for el in data:
        idx+=1
        
        if isinstance(el,int):
            count = el
            arr.extend(x * count)
            arr +=decode(data[idx::])
            return arr
        
    return arr
print(decode( ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]))
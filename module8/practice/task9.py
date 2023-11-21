def all_sub_lists(data):
    a= [[]]
    for el in range(len(data)):
        for i in range(el+1,len(data)+1):
            a.append(data[el:i])
    a.sort(key=len)
    return a
print(all_sub_lists([4, 6, 1, 3]))
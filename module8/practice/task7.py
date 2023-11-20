def data_preparation(list_data):
    a=[]
    for el in list_data:
        if len(el) >2:
            min_val = min(el)
            max_val = max(el)
            el.remove(min_val)
            el.remove(max_val)
        a+=el
    a.sort(reverse=True)
    return a
print(data_preparation([[1,2,3],[3,4], [5,6]]))
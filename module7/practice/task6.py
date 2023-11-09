def  get_recipe(path, search_id):
    
    with open(path, 'r') as fh:
        recepies = fh.readlines()
        str= ''
        for r in recepies:
            if r.find(search_id) == 0:
               str = r
            else:
                continue
        if str:
            a = str.split(',')
            str = {
                "id": a[0],
                "name": a[1],
                "ingredients": [
                    a[2],
                    a[3],
                    a[4].split('\n')[0],
            ],
}
        return str if bool(str) else None
        
    
print( get_recipe('recepies.txt', '60b90c3b13067a15887e1ae4'))
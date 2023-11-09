def get_cats_info(path):
    cats = []
    with open(path, 'r') as fh:
        raw_cats = fh.readlines()
        for cat in raw_cats:
            ar = cat.split(',')
            age = ar[2].split('\n')
            cats.append({"id": ar[0], "name": ar[1], "age":age[0] })
    return cats
print(get_cats_info('cats.txt'))
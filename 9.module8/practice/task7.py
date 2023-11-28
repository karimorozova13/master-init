import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    new_cats = []
    for cat in cats:
        if type(cat)== dict:
            new_cats.append(Cat(cat['nickname'],cat['age'],cat['owner']))
        else:
            new_cats.append({
                "nickname":cat.nickname,
                "age":cat.age,
                
                "owner":cat.owner,
                
            })
    return new_cats
print(convert_list([Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]))
print(convert_list([{'nickname': 'Mick', 'age': 5, 'owner': 'Sara'}, {'nickname': 'Barsik', 'age': 7, 'owner': 'Olga'}, {'nickname': 'Simon', 'age': 3, 'owner': 'Yura'}]))

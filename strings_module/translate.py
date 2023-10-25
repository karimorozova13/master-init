# replace symbol with map

map = {
    ord('К'):'K',
    ord('п'): 'p'
    }
translated = 'Кп'.translate(map)
print(translated)
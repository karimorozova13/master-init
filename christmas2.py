

with open('advent3.txt', 'r') as fh:
    data = fh.readlines()
    i =0
    obj ={}
    value =[]
    key =''
    for el in data:
        el = el.replace('\n', '')
        el= ' '.join(el.split(': '))
        if i == 0:
            l =el.split(' ')
            obj.update({l[0]:l[1::]})
            i +=1
            continue
        if el == '':
            del el
            continue
        if i ==1:
            key = el
            i +=1
            continue
        if ":" in el and i !=1:
            
            obj.update({key:value})
            value =[]
            key = el
            continue
        value.append(el)
            
            
obj.update({key:value}) 

seeds = obj['seeds']
new_seeds = []
new_seeds.append(seeds[:2])
new_seeds.append(seeds[2:4])
new_seeds.append(seeds[4:6])
new_seeds.append(seeds[6:8])
new_seeds.append(seeds[8:10])
new_seeds.append(seeds[10:12])
new_seeds.append(seeds[12:14])
new_seeds.append(seeds[14:16])
new_seeds.append(seeds[16:18])
new_seeds.append(seeds[18:20])
n_l =[]

for el in new_seeds:
    print(el)
    for i in range(int(el[0]), int(el[0])+int(el[1])):
        
        n_l.append(i)
print(n_l)
    
seed_to_soil_map = obj['seed-to-soil map:']
soil_to_fertilize_map = obj['soil-to-fertilizer map:']
fertilizer_to_water_map = obj['fertilizer-to-water map:']
water_to_light_map = obj['water-to-light map:']
light_to_temperature_map = obj['light-to-temperature map:']
temperature_to_humidity_map = obj['temperature-to-humidity map:']
humidity_to_location_map = obj['humidity-to-location map:']

print(seeds)
def convert_value(seed, arr_of_str ):
    output = seed 
    
    for num_range in arr_of_str:
        list_of_ranges = num_range.split(' ')
        output_start, start, step = map(int, list_of_ranges)
        
        if int(seed) in range(int(start), int(start) + int(step)):
            dif = int(seed) - int(start)
            output= int(output_start) + dif
            
            
    return output
        

last_obj = {}
last_index = 0

for el in n_l:
    
    soil = convert_value(el, seed_to_soil_map)
    fertilizer =convert_value(soil, soil_to_fertilize_map)
    water = convert_value(fertilizer, fertilizer_to_water_map)
    light = convert_value(water, water_to_light_map)
    temperature = convert_value(light, light_to_temperature_map)
    humidity = convert_value(temperature, temperature_to_humidity_map)
    location= convert_value(humidity, humidity_to_location_map)
    
    last_obj.update({
        last_index: {
            "seed": el,
            "soil": soil,
            "fertilizer": fertilizer,
            "water": water,
            "light": light,
            "temperature": temperature,
            "humidity": humidity,
            "location": location,
        }
    })
    last_index += 1
           
           
# print(last_obj)
l= []

for key, value in last_obj.items():
    l.append(value['location'])
print(min(l))   
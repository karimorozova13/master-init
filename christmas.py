import re

l= [79, 14, 55, 13]
v= 79

with open('advent.txt', 'r') as fh:
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
seed_to_soil_map = obj['seed-to-soil map:']
soil_to_fertilize_map = obj['soil-to-fertilizer map:']
fertilizer_to_water_map = obj['fertilizer-to-water map:']
water_to_light_map = obj['water-to-light map:']
light_to_temperature_map = obj['light-to-temperature map:']
temperature_to_humidity_map = obj['temperature-to-humidity map:']
humidity_to_location_map = obj['humidity-to-location map:']
print(seeds)
print(seed_to_soil_map, 'seed_to_soil_map')
print(soil_to_fertilize_map, 'soil_to_fertilize_map')
print(fertilizer_to_water_map, 'fertilizer_to_water_map')
print(water_to_light_map, 'water_to_light_map')
print(light_to_temperature_map, 'light_to_temperature_map')
print(temperature_to_humidity_map, 'temperature_to_humidity_map')
print(humidity_to_location_map, 'humidity_to_location_map')


output_list =[]

def convert_value(seed, str_of_ranges):
    idx = -1
    output = seed 
    for num_range in str_of_ranges:
        list_of_ranges = num_range.split(' ')
        source_range = list(range(int(list_of_ranges[1]), int(list_of_ranges[1])+ int(list_of_ranges[2])))
        target_range =list(range(int(list_of_ranges[0]), int(list_of_ranges[0])+ int(list_of_ranges[2])))
        if seed in source_range:
            idx = source_range.index(seed)
    return seed if idx == -1 else target_range[idx]

last_obj = {}
last_index = 0

for el in seeds:
    
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
           
           
print(last_obj)    
        
    
    
    
        
        
    

# print(data)
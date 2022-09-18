"""
07_dictionary commprehension
"""
# new_dictionary = {key: value for (key,value) in iterable}

#items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}
#items_in_meters = {key: value for (key, value) in items_in_cm.items()}
#items_in_meters = {key + ' in meters': value/100 for (key, value) in items_in_cm.items()}

#print(items_in_meters)
# {'pen': 0.4, 'book': 0.5, 'keyboard': 0.6}

#developers = {'Jane': 'Python', 'Jade': 'JavaScript', 'John': 'Python', 'Doe': 'JavaScript'}

#python_developers = {key: value for (key, value) in developers.items() if value == 'Python'}

#print(python_developers)

numbers = {10: 30, 99: 20, 73: 5}

item_in_num = [key for (key, value) in numbers.items() if key == 10]

print(item_in_num)
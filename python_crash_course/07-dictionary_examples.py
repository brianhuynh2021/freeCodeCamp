"""
07_dictionary commprehension
"""
# new_dictionary = {key: value for (key,value) in iterable}

items_in_cm = {'pen': 40, 'book': 50, 'keyboard': 60}
items_in_meters = {key: value/100 for (key, value) in items_in_cm.items()}

print(items_in_meters)
# {'pen': 0.4, 'book': 0.5, 'keyboard': 0.6}

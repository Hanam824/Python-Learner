# define default value in Dictionaries with .get() and .setdefault()

my_dict = {"item": "football", "price": 10.0}

# "count" is not a key in dictionary, so the return value will be None.
count = my_dict.get("count")
print(count)

# we specify 0 is default return value if the key is not in dictionary.
count1 = my_dict.get("count", 0)
print(count1)

#  .setdefault() will make this key available in dictionary
count2 = my_dict.setdefault("count", 0)
print(count2)
print(my_dict)


# merge 2 dictionary
d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}

# version 3.5+
merged_dict = {**d1, **d2}
print(merged_dict)

# version 3.9+
merged_dict = d1 | d2
print(merged_dict)

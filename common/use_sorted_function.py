# sort complex iterables with sorted()

# sort with reverse type
raw_data = [3, 5, 1, 10, 9]
sorted_data = sorted(raw_data, reverse=True)
print(sorted_data)

# with list of dictionary, sort by "age"
raw_data = [
    {"name": "Alex", "age": 20},
    {"name": "Lisa", "age": 6},
    {"name": "Ben", "age": 119},
]
sorted_data = sorted(raw_data, key=lambda x: x["age"])
print(sorted_data)

# sort by list function will change list itself
raw_data.sort(key=lambda x: x["name"])
print(raw_data)

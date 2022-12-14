# iterate with enumerate() instead of range(lend())

raw_data = [1, 2, -1, -4, 5, 11, -0.5, 25]

# simple
for idx in range(len(raw_data)):
    if raw_data[idx] < 0:
        raw_data[idx] == 0
print(raw_data)

# pro
for idx, data in enumerate(raw_data):
    if data < 0:
        raw_data[idx] = 0
print(raw_data)

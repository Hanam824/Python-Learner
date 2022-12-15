search_list = [1, 3, 5, 6, 36, 98, 4, 58, 4, 5]
target = 4

# simple way
found = False
for element in search_list:
    if element == target:
        print("I found it!")
        found = True
        break
if not found:
    print("I din't find it")

# pro
for idx, element in enumerate(search_list):
    if element == target:
        print(f"I found it!. It is the number {idx} in search list.")
        break
else:
    print("I din't find it")

# or loop with while
idx = 0
while idx < len(search_list):
    if search_list[idx] == target:
        print(f"I found it!. It is the number {idx} in search list.")
        break
    idx += 1
else:
    print("I din't find it")

tup = (1, 2, 3, 8, 6)

list = [1, 7, 8, 2]

string = "hello"

my_dict = {"name": "Alex", "age": 18}

# error
# num1, num2, num3, num4 = tup
num1, num2, num3, num4, num5 = tup

ls1, ls2, ls3, ls4 = list

key1, key2 = my_dict.items()
print(key1, key2)

key1, key2 = my_dict.values()
print(key1, key2)


##### multiple assigment
width, height = 400, 200
print(width, height)
width, height = height, width
print(width, height)

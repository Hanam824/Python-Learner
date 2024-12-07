########################################################
#  BASIC
lst = [1,2,3,3.4,23.43, 'Jybra', True]

# print first element
print(lst[0])

# print last element
print(lst[-1])

lst1 = [1,3,5,[3,4,5]]

# print 2nd in 3 element
print(lst1[3][1])

lst2 = lst + lst1
print(lst2)

for i in lst2:
    print(i)

print('-------------------------')
# find 23.43 in lst2
print(23.43 in lst2)
print('-------------------------')

########################################################
#  ADVANCE
# Use list comprehension instead of for raw loops

# simple
squares = []
for idx in range(10):
    squares.append(idx * idx)
print(squares)

# pro
squares = [idx * idx for idx in range(10)]
print(squares)

zeros = [[0 for _ in range(2)] for _ in range(4)]
print(zeros)

x = (i for i in "hello")
print(tuple(x))
print(list(x))


#
sentence = "hello world"
x = {char: sentence.count(char) for char in set(sentence)}
print(x)

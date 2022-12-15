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

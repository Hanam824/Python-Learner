# Use list comprehension instead of for raw loops

# simple
squares = []
for idx in range(10):
    squares.append(idx * idx)
print(squares)

# pro
squares = [idx * idx for idx in range(10)]
print(squares)

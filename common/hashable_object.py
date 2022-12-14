# count hasable obj collection.
from collections import Counter

my_list = [10, 10, 10, 5, 5, 2, 9, 9, 9, 9, 9]
counter = Counter(my_list)

most_common = counter.most_common(2)
# print(most_common)
print(most_common[0])

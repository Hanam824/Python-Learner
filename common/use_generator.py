# Save memory with generator
import sys

raw_list = [num for num in range(10000)]
print(sum(raw_list))
print(sys.getsizeof(raw_list), "bytes")

gen_list = (num for num in range(10000))
print(sum(gen_list))
print(sys.getsizeof(gen_list), "bytes")

# Pipelining Generators
# We should use yield when we want to iterate over a sequence,
# but don’t want to store the entire sequence in memory
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num**2


print(sum(square(fibonacci_numbers(10))))
# lst_gen = list(square(fibonacci_numbers(10)))

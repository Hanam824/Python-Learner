import itertools

def generate_permutation(n, r):
    """
    Generate permutations of n elements taken r at a time.

    Args:
        n (int): Total number of elements.
        r (int): Number of elements to take at a time.

    Returns:
        list: List of permutations.
    """
    # Get user input for n and r
    n = int(input("Enter total number of elements (n): "))
    r = int(input("Enter number of elements to take at a time (r): "))

    # Generate permutations
    perms = list(itertools.permutations(range(n), r))

    return perms

# Example usage:
perms = generate_permutation(5, 3)
print(perms)
# Bit Sorting

# In this problem, you are expected to sort an array of integers in ascending order based on the number of their illuminated bits.

# Input:
# You will receive n integers separated by a single space in the only line of input.

# Output:
# Display the sorted list in the only line of output.

# Example 1:
# Input:
# 7 6 15 8
# Output:
# [8, 6, 7, 15]

# Explanation:
# 7 has three illuminated bits (0111).
# 6 has two illuminated bits (0110).
# 15 has four illuminated bits (1111).
# 8 has one illuminated bit (1000).
# Therefore, the list is sorted as [8, 6, 7, 15].

# Note: In cases where two numbers have the same number of bits, compare their actual values. For example, between 10 (1010) and 12 (1100), both have the same number of bits, which is 2. However, 10 is less than 12, so it comes before 12 in the list.

# Example 2:
# Input:
# 3 8 3 6 5 7 9 1
# Output:
# [1, 8, 3, 3, 5, 6, 9, 7]


def num_ones(number):
    bin_string = bin(number)

    ind = bin_string.index("b")

    bin_num = list(bin_string[ind + 1 :])

    num_ones = sum(list(map(int, bin_num)))

    return num_ones


str = list(input().split())

numbers = list(map(int, str))

numbers = sorted(numbers)

print(sorted(numbers, key=num_ones))

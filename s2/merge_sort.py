# Recursive Sorting

# In this problem, you are expected to sort an array of integers in ascending order using a recursive function and the merge sort algorithm.

# Input
# In the only line of input, you will receive n integers separated by a single space.

# Output
# Print the left side of the array before sorting in each row, and in the final row, print the sorted array.

# Example 1:
# Input
# 12 11 13 5 6 7
# Output
# [11]
# [12]
# [6]
# [5]
# [11, 12, 13]
# [5, 6, 7, 11, 12, 13]

# Example 2:
# Input
# 5 3 8 4 2 7 1 9
# Output
# [5]
# [8]
# [3, 5]
# [2]
# [1]
# [2, 7]
# [3, 4, 5, 8]
# [1, 2, 3, 4, 5, 7, 8, 9]


def merge(left_list, right_list):
    i = 0
    j = 0

    merged_list = []
    print(left_list)
    while (i < len(left_list)) and (j < len(right_list)):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1

    for ii in range(i, len(left_list)):
        merged_list.append(left_list[ii])

    for jj in range(j, len(right_list)):
        merged_list.append(right_list[jj])

    return merged_list


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    low = 0
    high = len(input_list)

    mid = low + high // 2

    left = input_list[low:mid]

    right = input_list[mid:high]
    sorted_left = merge_sort(left)

    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


# main body of the program

input_list = list(map(int, input().split()))

sorted_list = merge_sort(input_list)

print(sorted_list)

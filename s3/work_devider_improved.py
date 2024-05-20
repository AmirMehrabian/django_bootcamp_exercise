# Task Distribution

# Kambiz and Shahram, who are teammates for various course projects,
# have decided to divide the projects between themselves.
# Since Shahram is much more professional than Kambiz, he has decided
# to take on almost twice as much work as Kambiz. Note that each project
# has a difficulty level denoted by \( d_i \).

# They want to divide all the projects between themselves in such
# a way that the difference between the total difficulty of the
# projects done by Shahram and twice the total difficulty of
# the projects done by Kambiz is minimized.

# Input
# - The first line contains the integer \( n \), followed by \( n \)
# lines each containing one integer representing the difficulty level
# of each project \( d_i \).

# \( 0 \leq n \leq 100 \)

# \( 0 \leq d_i \leq 500 \)

# ### Output
# - Print the minimum possible difference in one line.

# ### Sample Input 1
# ```
# 3
# 2
# 3
# 5
# ```

# ### Sample Output 1
# ```
# 1
# ```
# Explanation: If Kambiz only takes the second project and
# Shahram takes the remaining projects, the best possible case is
# achieved and the answer is \( |(3*2) - 7| = 1 \).

# ### Sample Input 2
# ```
# 4
# 1
# 2
# 4
# 6
# ```

# ### Sample Output 2
# ```
# 1
# ```

# Explanation: The best possible case is achieved and
# the answer is \( |(2 + 6) - 2 * (1 + 4)| = 1 \).


def min_diff_subsets(main_set, verbose=False):
    num_col = sum(main_set)
    num_row = len(main_set)

    dp_table = [[False] * (num_col + 1) for _ in range(num_row + 1)]

    for i in range(num_row + 1):
        dp_table[i][0] = True

    for row in range(1, num_row + 1):
        for col in range(1, num_col + 1):
            if dp_table[row - 1][col]:
                dp_table[row][col] = True
            elif col >= main_set[row - 1]:
                dp_table[row][col] = dp_table[row - 1][col - main_set[row - 1]]

    sum_of_subset1 = [i for i in range(num_col + 1) if dp_table[num_row][i]]
    min_diff = min(abs(2 * num_col - 3 * s) for s in sum_of_subset1)

    if verbose:
        print("DP table:\n")
        for row in range(num_row + 1):
            for col in range(num_col + 1):
                print(dp_table[row][col], end=" | ")
            print("\n")

        print(f"Possible sums of subset 1: {sum_of_subset1}")
        possible_diffs = [abs(2 * num_col - 3 * s) for s in sum_of_subset1]
        print(f"Possible differences in sum of subsets: {possible_diffs}")
        print(f"Minimum difference in sum of subsets: {min_diff}")

    return min_diff


num_inputs = int(input())
list_input = []
for ii in range(num_inputs):
    inputs = int(input())
    list_input.append(inputs)


print(min_diff_subsets(list_input))

# Price Estimation

# In this question, we aim to predict the price of a house by receiving
# its specifications and using the data available to us.

# Information
# To predict the price of new houses, you should use the data provided
# below. This data consists of two parts: the first part is the house
# specifications, and the second part is the price of that house.
# The elements of the first part are as follows:

# House area (square meters)
# Number of rooms
# Number of bathrooms
# Distance to the shopping center (kilometers)
# house_info = [
#     ((150, 3, 2, 1), 450),
#     ((200, 4, 3, 0.5), 600),
#     ((100, 2, 1, 2), 300),
#     ((250, 5, 4, 1.5), 800),
#     ((180, 4, 2, 3), 550),
#     ((220, 3, 3, 2), 700),
#     ((120, 2, 1, 4), 400),
#     ((300, 6, 4, 2.5), 900),
#     ((170, 3, 2, 0.8), 500),
#     ((230, 4, 3, 3.5), 750),
#     ((210, 4, 2, 2), 650),
#     ((140, 3, 2, 1.2), 480),
#     ((270, 5, 3, 2.2), 820),
#     ((190, 4, 2, 4), 600),
#     ((260, 4, 3, 1), 780),
#     ((130, 3, 1, 3), 350),
#     ((240, 5, 3, 0.7), 720),
#     ((280, 6, 4, 3), 850),
#     ((160, 3, 2, 1.5), 520),
#     ((290, 5, 3, 2.8), 880)
# ]
# Plain text
# Input
# The first line of the input provides the specifications of a house,
# separated by spaces.

# The second line provides a number K that specifies the number of comparable
# samples, and the estimated price is based on the highest price among the K 
# samples that have the closest distance to the input. 
#The following condition for K is also maintained:

# 2 ≤ k ≤ 20

# Output
# In the only output line, you should display an integer representing
# the price of the new house.

# Example
# Input
# 170 3 2 0.8
# 3
# Plain text
# Output
# 550


import numpy


def diff_finder(target, house_info):
    diff_house = []
    for ii in house_info:
        x = numpy.linalg.norm(numpy.array(ii[0]) - target)
        diff_house.append([x, ii[1]])

    diff_house = sorted(diff_house, key=lambda x: x[0])

    return diff_house


def estimator(diff_house, k):
    similar_house_price = [diff_house[ii][1] for ii in range(k)]
    estimated_price = max(similar_house_price)

    return estimated_price


house_info = [
    ((150, 3, 2, 1), 450),
    ((200, 4, 3, 0.5), 600),
    ((100, 2, 1, 2), 300),
    ((250, 5, 4, 1.5), 800),
    ((180, 4, 2, 3), 550),
    ((220, 3, 3, 2), 700),
    ((120, 2, 1, 4), 400),
    ((300, 6, 4, 2.5), 900),
    ((170, 3, 2, 0.8), 500),
    ((230, 4, 3, 3.5), 750),
    ((210, 4, 2, 2), 650),
    ((140, 3, 2, 1.2), 480),
    ((270, 5, 3, 2.2), 820),
    ((190, 4, 2, 4), 600),
    ((260, 4, 3, 1), 780),
    ((130, 3, 1, 3), 350),
    ((240, 5, 3, 0.7), 720),
    ((280, 6, 4, 3), 850),
    ((160, 3, 2, 1.5), 520),
    ((290, 5, 3, 2.8), 880),
]

target = list(input().split())
target = list(map(float, target))
k = int(input())

diff_list = diff_finder(target, house_info)
print(estimator(diff_list, k))

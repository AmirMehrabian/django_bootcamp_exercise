
def num_ones(number):
   
   bin_string = bin(number)

   ind = bin_string.index('b')

   bin_num = list(bin_string[ind + 1:])

   num_ones = sum(list(map(int,bin_num)))

   return num_ones

str = list(input().split())

numbers = list(map(int, str))

numbers = sorted(numbers)

print(sorted(numbers, key=num_ones))

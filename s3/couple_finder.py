# Pair Pair

# Maryam, who has recently started working as a manager at Quera, wants to help
# two suitable young people find a good match on her first working day.
# After a lot of thinking and investigation, Maryam found a special method to
# evaluate the compatibility and suitability of two young individuals.
# Maryam logically concluded:

# The longer the common subsequence between the names of the two young people,
# the more stable their shared life will be.

# Since Maryam is very busy and does not have enough time to check the length
# of the subsequences, she has asked you to help her. She wants you to choose
# the most suitable option for marriage for each person she introduces.

# Input
# In the first line of input, the name of the person Maryam is interested in
# is entered.

# In the next line, the number n is entered, indicating the number of available
# candidates.

# In the next n lines, the names of the candidates are entered.

# It is guaranteed that all names are written in lowercase letters and the length
# of each string is less than or equal to 100.

# 1 ≤ length(name), n ≤ 100

# Output
# The output of your program should include 2 lines: the first line should contain
# the common subsequence of the name of Maryam's interested person and the chosen
# candidate's name, and the second line should contain the length of this
# subsequence.

# Example
# Sample Input 1
# farideh
# 3
# gholam
# arshia
# ahmad
# Plain text
# Sample Output 1
# arh
# 3
# Plain text
# Explanation of the example:

# The length of the longest common subsequence between farideh and
# gholam is 1. ("a" or "h")

# The length of the longest common subsequence between farideh and
# arshia is 3. ("arh")

# The length of the longest common subsequence between farideh and
# ahmad is 2. ("ah")

# Therefore, the longest common subsequence is between farideh and
# arshia.
# 


def longest_subseq(name1, name2, verbose = False):
        l_name1 = len(name1)
        l_name2 = len(name2)
        
        dp_table  = [[0]*(l_name2 + 1) for _ in range(l_name1+1)]
        
        indexes = []
        
        for row in range(1, l_name1+1):
            for col in range(1, l_name2+1):
               
                condition = name1[row-1] == name2[col-1]
                term = max(dp_table[row-1][col], dp_table[row][col-1])
                term1 = term
                if condition :
                    term = dp_table[row-1][col-1] + 1
        
                dp_table[row][col] = term 
                

        if verbose:
            print('     ', end = ' | ')
            for char in name2:
                print(char, end = ' | ',)
            
            
            print()
            table_name =' '+ name1
            for ii in range(l_name1+1):
                print(table_name[ii], end= ' | ') 
                
                for jj in range(l_name2+1):
                    print(dp_table[ii][jj], end=' | ')
            
                print()
                
        longest_seq = []
        row, col = l_name1, l_name2
        
        while row > 0 and col > 0:
            if name1[row-1] == name2[col-1]:
                longest_seq.append(name1[row-1])
                row -= 1
                col -= 1
            elif dp_table[row-1][col] > dp_table[row][col-1]:
                row -= 1
            else:
                col -= 1
        
        longest_len = dp_table[l_name1][l_name2]

        longest_seq.reverse()
        longest_seq_str = ''.join(longest_seq)


        return longest_len, longest_seq_str
                

name1 = input()

num_targest = int(input())

target_list = []
for _ in range(num_targest):
    target = input()
    target_list.append(target)


max_len = 0
best_target =''
for target_name in target_list:
    (len_seq, similar_seq) = longest_subseq(name1, target_name)
    
    if max_len < len_seq:
        max_len = len_seq
        best_target = similar_seq
        

print(best_target) 
print(max_len)
       
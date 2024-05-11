# Anti-virus

# Vahid, who does not have much knowledge in using computers, thinks that his personal system has been infected. He asks you to write a program for him that receives the full name of a file, including the file name and its extension, and based on the file extension, determines whether the file is malicious or not.

# To solve this problem, we assume that in the ideal case, the length of the extension of all healthy files is 3 characters. Therefore, if the length of the file extension is less than or more than 3 characters, the word "Warning" should be printed in the output, otherwise "Ok" should be printed.

# *Note that the file name and its extension separated by a dot .*

# Input
# Only one line of input containing the name of a file along with its extension, separated by a dot, is given to the program.

# Output
# Only one line of output is enough to display the word "Warning" or "Ok" according to the desired conditions.

# Example
# Sample Input 1
# test1.exe
# Sample Output 1
# Ok

# Sample Input 2
# test1.xyzc
# Sample Output 2
# Warning

# Note
# It is guaranteed that there is only one dot in the input!


str1 = input()

ind = str1.index('.')

l = len(str1[ind+1:])

print("Ok" if l==3 else "Warning")
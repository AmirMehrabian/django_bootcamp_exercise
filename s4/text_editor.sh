#Elegant Display

#In this exercise, we will write a simple file viewer using the awk command.

#For this exercise, we have a file called data.txt with the first few lines as follows:

#data.txt
#a|12|1
#b|22|2
#c|32|3
#d|42|41
#e|52|534
#f|62|676
#g|72|8
#h|82|9
#i|92|0
#We want to display the entire contents of this file in a neat format in the terminal.

#To solve this exercise, you need to display the contents of this file in the following format using the awk command in one line:

#terminal
#col1 - col2 - col3
#a - 12 - 1
#b - 22 - 2
#c - 32 - 3
#d - 42 - 41
#e - 52 - 534
#f - 62 - 676
#g - 72 - 8
#h - 82 - 9
#i - 92 - 0
#1274
#As you can see in the output above, the first line should display the three columns col1, col2, and col3 first. Then, after displaying the contents of the file, the last line of the output should display the sum of the values in the third column.

#Note

#You must write the requested command in one line only.
#The values in the question only show a part of the original file, and the original file has many values.
#We recommend that you see the answer to the question after solving the exercise.

awk -F "|" 'BEGIN {print "col1 - col2 - col3"} { print   $1" - "$2" - "$3 ; sum+=$3 } END {print sum}' data.txt


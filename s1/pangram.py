#pangram
START = 65

END = 90

ALPHABET_SIZE = 26

alphabets =  set([chr(char) for char in range(START, END+1)])

str = set(input().upper())

union = alphabets & str


print("pangram" if len(union) == ALPHABET_SIZE else "not pangram")
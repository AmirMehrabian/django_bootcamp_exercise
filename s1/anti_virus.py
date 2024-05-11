str1 = input()

ind = str1.index('.')

l = len(str1[ind+1:])


print("Ok" if l==3 else "Warning")
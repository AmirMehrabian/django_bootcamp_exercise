str = input().split()

numbers = list(map(float, str))

l = len(numbers)

agg = sum(numbers)

avg = agg/l

max_num = max(numbers)

min_num = min(numbers)

answer = f"{avg:.2f} {min_num:.2f} {max_num:.2f}  {agg:.2f}"

print(answer)
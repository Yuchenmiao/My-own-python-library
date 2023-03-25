stones = str(input())
length = len(stones)
i = 0
while i < length - 1 :
    if str(stones[i]) == str(stones[i+1]) :
        stones = stones[:i]+stones[i+2:]
        length = len(stones)
        i = 0
        continue
    else :
        i = i + 1
print(stones)
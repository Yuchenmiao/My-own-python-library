i = int(input())
sum = 0
m = 0
if i % 2 == 1 :
    while m < i :
        sum = sum + ((i - 1) ** 2 / 2 + 2 * m + 1) ** 2
        m = m + 1
elif i % 2 == 0 :
    while m < i :
        sum = sum + (i * (i - 2) / 2 + 2 * m + 2) ** 2
        m = m + 1
else :
    None
print(int(sum))
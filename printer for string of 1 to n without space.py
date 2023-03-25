n = int(input())
list = []

for i in range(1,n+1) :
    list = list+[i]

stri = ''
for j in list :
    stri = stri + str(j)

print(stri)
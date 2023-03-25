list_stk = eval(input())
list_ins = eval(input())
n = len(list_stk)
m = len(list_ins)
# "flip" the "pancake"
for i in range (m) : # i refer to the ith number in list_ins
    Spatula = int(list_ins[i]) # Where to flip the pancake
    list_flipped = list_stk[:Spatula][::-1]
    list_stk = list_flipped + list_stk[Spatula:n]
# estimate whether or not the list is in ascending order
judgement = "YES"
order = 0
while order >= 0 and order < n-1 :
    if int(list_stk[order]) <= int(list_stk[order+1]):
        order = order + 1
    else:
        judgement = "NO"
        break
print(list_stk)
print(judgement)
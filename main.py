n = int(input('Your grades:'))
k = 0
sum = 0
for i in range(n):
    m = int(input())
    k +=1
    sum += m
    formula = sum/k
print('Their arhimetic mean is =', formula)
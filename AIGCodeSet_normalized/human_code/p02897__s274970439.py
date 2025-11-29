v1 = int(input())
if v1 % 2 == 1:
    v2 = v1 // 2 + 1
else:
    v2 = v1 // 2
print('{:.10f}'.format(v2 / v1))

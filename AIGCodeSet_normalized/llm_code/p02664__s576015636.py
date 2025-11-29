v1 = input()
if '?' in v1:
    v1 = v1.replace('?', 'D')
    v2 = v1.replace('?', 'P')
    v3 = v2.count('D') + v2.count('PD')
    v4 = v1.count('D') + v1.count('PD')
    v1 = v2 if v3 > v4 else v1
print(v1)

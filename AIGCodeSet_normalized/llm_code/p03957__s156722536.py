v1 = input()
v2 = True
if 'C' not in v1 or 'F' not in v1:
    v2 = False
print('Yes' if v1.index('C') < v1.rindex('F') and v2 == True else 'No')

v1 = input()
print('Yes' if len(set(v1)) == 2 and v1.count(v1[0]) == 2 else 'No')

v1 = input()
if 'N' in v1 and 'S' not in v1 or ('S' in v1 and 'N' not in v1) or ('E' in v1 and 'W' not in v1) or ('W' in v1 and 'E' not in v1):
    print('No')
else:
    print('Yes')

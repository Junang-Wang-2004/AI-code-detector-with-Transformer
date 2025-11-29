import re
v1 = str(input())
v2 = 'A.*Z'
v3 = re.search(v2, v1)
print(len(v3.group()))

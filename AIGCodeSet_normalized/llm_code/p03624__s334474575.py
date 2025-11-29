v1 = list(input())
import string
v2 = list(string.ascii_lowercase)
for v3 in v2:
    if v3 not in v1:
        print(v3)
        break
else:
    print('None')

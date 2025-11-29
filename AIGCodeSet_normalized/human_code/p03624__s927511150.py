v1 = input()
v2 = []
for v3 in range(97, 123):
    if chr(v3) not in v1:
        v2.append(chr(v3))
        print(chr(v3))
        break
if len(v2) == 0:
    print('None')

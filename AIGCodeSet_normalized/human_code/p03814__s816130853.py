v1 = input()
v2 = v1.find('A')
v3 = v1[::-1].find('Z')
print(len(v1) - v2 - v3)

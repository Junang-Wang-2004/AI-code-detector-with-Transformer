v1 = input()
for v2 in range(97, 97 + 26):
    if chr(v2) not in v1:
        print(chr(v2))
        break
else:
    print(None)

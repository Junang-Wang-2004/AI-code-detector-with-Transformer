int(input())
list = [s]
v1 = 2
while v1 <= 1000000:
    if v1 % 2 == 0:
        list.append(list[v1 - 2] / 2)
    else:
        list.append(list[v1 - 2] * 3 + 1)
    if list[v1 - 1] in list[:v1 - 1]:
        break
    v1 += 1
print(v1)

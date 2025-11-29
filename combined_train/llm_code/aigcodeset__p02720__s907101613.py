v1 = int(input())
v2 = 0

def f1(a1, a2, a3, a4):
    global count
    global k
    if a2 == 1:
        if a3:
            v1 += 1
            if v1 == v1:
                print(a4.replace('0', ''))
                return True
    elif a1 == 0:
        if a3 == False:
            if f1(0, a2 - 1, False, a4 + str(0)):
                return True
            for v2 in range(1, 10):
                if f1(v2, a2 - 1, True, a4 + str(v2)):
                    return True
        else:
            if f1(a1, a2 - 1, True, a4 + str(a1)):
                return True
            if f1(a1 + 1, a2 - 1, True, a4 + str(a1 + 1)):
                return True
    elif a1 == 9:
        if f1(a1 - 1, a2 - 1, True, a4 + str(a1 - 1)):
            return True
        if f1(a1, a2 - 1, True, a4 + str(a1)):
            return True
    else:
        if f1(a1 - 1, a2 - 1, True, a4 + str(a1 - 1)):
            return True
        if f1(a1, a2 - 1, True, a4 + str(a1)):
            return True
        if f1(a1 + 1, a2 - 1, True, a4 + str(a1 + 1)):
            return True
f1(0, 11, False, '0')

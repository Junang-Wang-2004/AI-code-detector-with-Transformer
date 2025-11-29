import bisect

def f1(a1, a2, a3):

    def reverse(a1, a2, a3):
        v1, v2 = (a2, a3 - 1)
        while v1 < v2:
            a1[v1], a1[v2] = (a1[v2], a1[v1])
            v1 += 1
            v2 -= 1
    v1, v2 = (a2 - 1, a2)
    for v3 in reversed(range(a2, a3 - 1)):
        if a1[v3] < a1[v3 + 1]:
            v1 = v3
            break
    else:
        reverse(a1, a2, a3)
        return False
    for v3 in reversed(range(v1 + 1, a3)):
        if a1[v3] > a1[v1]:
            v2 = v3
            break
    a1[v1], a1[v2] = (a1[v2], a1[v1])
    reverse(a1, v1 + 1, a3)
    return True

def f3():

    def f(a1):
        v1 = []
        v2 = ''
        for v3 in range(9):
            if a1 & 1 << v3 == 0:
                continue
            if (v3 + 1) % 2:
                if v2:
                    return (v1, v2, False)
                v2 = str(v3 + 1)
            v1.extend([str(v3 + 1)] * ((v3 + 1) // 2))
        return (v1, v2, True)
    v1 = []
    for v2 in range(1, 1 << 9):
        v3, v4, v5 = f(v2)
        if not v5:
            continue
        while True:
            v6 = ''.join(v3)
            v7 = v6 + v4 + v6[::-1]
            if len(v7) > MAX_LEN:
                break
            v1.append(int(v7))
            if not f1(v3, 0, len(v3)):
                break
    v1.sort()
    return v1
v1 = 16
v2 = f3()

class C1(object):

    def specialPalindrome(self, a1):
        """
        """
        return v2[bisect.bisect_right(v2, a1)]

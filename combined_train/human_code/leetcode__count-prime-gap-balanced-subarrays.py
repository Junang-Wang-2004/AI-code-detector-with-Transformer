import collections

def f1(a1):
    v1 = []
    v2 = [-1] * (a1 + 1)
    for v3 in range(2, a1 + 1):
        if v2[v3] == -1:
            v2[v3] = v3
            v1.append(v3)
        for v4 in v1:
            if v3 * v4 > a1 or v4 > v2[v3]:
                break
            v2[v3 * v4] = v4
    return v2
v1 = 5 * 10 ** 4
v2 = f1(v1)

class C1(object):

    def primeSubarray(self, a1, a2):
        """
        """
        v1, v2, v3 = (collections.deque(), collections.deque(), collections.deque())
        v4 = v5 = 0
        for v6 in range(len(a1)):
            if v2[a1[v6]] == a1[v6]:
                v1.append(v6)
                while v2 and a1[v2[-1]] <= a1[v6]:
                    v2.pop()
                v2.append(v6)
                while v3 and a1[v3[-1]] >= a1[v6]:
                    v3.pop()
                v3.append(v6)
                while a1[v2[0]] - a1[v3[0]] > a2:
                    if v3[0] == v5:
                        v3.popleft()
                    if v2[0] == v5:
                        v2.popleft()
                    if v1[0] == v5:
                        v1.popleft()
                    v5 += 1
            if len(v1) >= 2:
                v4 += v1[-2] - v5 + 1
        return v4

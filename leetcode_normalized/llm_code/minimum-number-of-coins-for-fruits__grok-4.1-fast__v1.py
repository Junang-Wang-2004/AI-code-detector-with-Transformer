import collections

class C1(object):

    def minimumCoins(self, a1):
        v1 = len(a1)
        v2 = 10 ** 18 + 5
        v3 = [v2] * (v1 + 1)
        v3[0] = 0
        v4 = collections.deque()
        for v5 in range(v1):
            v6 = v3[v5] + a1[v5]
            while v4 and v3[v4[-1]] + a1[v4[-1]] >= v6:
                v4.pop()
            v4.append(v5)
            v7 = v5 // 2
            while v4 and v4[0] < v7:
                v4.popleft()
            v3[v5 + 1] = v3[v4[0]] + a1[v4[0]]
        return v3[-1]

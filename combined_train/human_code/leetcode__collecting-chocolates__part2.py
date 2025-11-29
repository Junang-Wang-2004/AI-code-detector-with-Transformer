import collections

class C1(object):

    def minCost(self, a1, a2):
        """
        """

        def cost(a1):
            v1 = a1 + 1
            v2 = a2 * a1
            v3 = collections.deque()
            for v4 in range(len(a1) + v1 - 1):
                if v3 and v4 - v3[0] == v1:
                    v3.popleft()
                while v3 and a1[v3[-1] % len(a1)] >= a1[v4 % len(a1)]:
                    v3.pop()
                v3.append(v4)
                if v4 >= v1 - 1:
                    v2 += a1[v3[0] % len(a1)]
            return v2

        def check(a1):
            return cost(a1) <= cost(a1 + 1)
        v1, v2 = (0, len(a1))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return cost(v1)

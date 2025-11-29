import collections

class C1(object):

    def maxProduct(self, a1):
        """
        """

        def manacher(a1):
            a1 = '^#' + '#'.join(a1) + '#$'
            v2 = [0] * len(a1)
            v3, v4 = (0, 0)
            for v5 in range(1, len(a1) - 1):
                v6 = 2 * v3 - v5
                if v4 > v5:
                    v2[v5] = min(v4 - v5, v2[v6])
                while a1[v5 + 1 + v2[v5]] == a1[v5 - 1 - v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3, v4 = (v5, v5 + v2[v5])
            return v2
        v1 = manacher(a1)
        v2 = collections.deque()
        v3 = [0]
        for v4 in range(len(a1)):
            while v2 and v2[0][1] < v4:
                v2.popleft()
            v3.append(max(v3[-1], 1 + 2 * (v4 - v2[0][0]) if v2 else 1))
            v2.append((v4, v4 + v1[2 * v4 + 2] // 2))
        v2 = collections.deque()
        v5 = v6 = 0
        for v4 in reversed(range(len(a1))):
            while v2 and v2[0][1] > v4:
                v2.popleft()
            v6 = max(v6, 1 + 2 * (v2[0][0] - v4) if v2 else 1)
            v2.append((v4, v4 - v1[2 * v4 + 2] // 2))
            v5 = max(v5, v3[v4] * v6)
        return v5

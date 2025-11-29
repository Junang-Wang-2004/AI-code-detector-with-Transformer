import collections

class C1(object):

    def minMaxSubarraySum(self, a1, a2):
        """
        """

        def count(a1):
            v1 = v2 = 0
            v3 = collections.deque()
            for v4 in range(len(a1)):
                v5 = v4
                while v3 and (not a1(a1[v3[-1][0]], a1[v4])):
                    v6, v5 = v3.pop()
                    v2 -= (v6 - v5 + 1) * a1[v6]
                v3.append([v4, v5])
                v2 += (v4 - v5 + 1) * a1[v4]
                v1 += v2
                if v4 - (a2 - 1) >= 0:
                    v2 -= a1[v3[0][0]]
                    if v3[0][0] == v4 - (a2 - 1):
                        v3.popleft()
                    else:
                        assert v3[0][1] == v4 - (a2 - 1)
                        v3[0][1] += 1
            return v1
        return count(lambda a, b: a < b) + count(lambda a, b: a > b)

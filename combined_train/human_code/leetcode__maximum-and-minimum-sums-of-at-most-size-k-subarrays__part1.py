import collections

class C1(object):

    def minMaxSubarraySum(self, a1, a2):
        """
        """

        def count(a1):
            v1 = v2 = 0
            v3 = collections.deque()
            for v4 in range(len(a1)):
                while v3 and (not a1(a1[v3[-1]], a1[v4])):
                    v5 = v3.pop()
                    v6 = v5 - (v3[-1] + 1 if v3 else max(v4 - a2 + 1, 0)) + 1
                    v2 -= v6 * a1[v5]
                v6 = v4 - (v3[-1] + 1 if v3 else max(v4 - a2 + 1, 0)) + 1
                v3.append(v4)
                v2 += v6 * a1[v4]
                v1 += v2
                if v4 - (a2 - 1) >= 0:
                    v2 -= a1[v3[0]]
                    if v3[0] == v4 - (a2 - 1):
                        v3.popleft()
            return v1
        return count(lambda a, b: a < b) + count(lambda a, b: a > b)

import collections

class C1(object):

    def continuousSubarrays(self, a1):
        """
        """
        v1 = v2 = 0
        v3, v4 = (float('inf'), float('-inf'))
        for v5 in range(len(a1)):
            if v3 <= a1[v5] <= v4:
                v3, v4 = (max(v3, a1[v5] - 2), min(v4, a1[v5] + 2))
            else:
                v3, v4 = (a1[v5] - 2, a1[v5] + 2)
                for v2 in reversed(range(v5)):
                    if not v3 <= a1[v2] <= v4:
                        break
                    v3, v4 = (max(v3, a1[v2] - 2), min(v4, a1[v2] + 2))
                else:
                    v2 = -1
                v2 += 1
            v1 += v5 - v2 + 1
        return v1

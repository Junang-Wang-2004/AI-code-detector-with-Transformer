import collections

class C1(object):

    def maxSelectedElements(self, a1):
        """
        """
        a1.sort()
        v1 = collections.defaultdict(int)
        v1[a1[0]] = v1[a1[0] + 1] = 1
        for v2 in range(1, len(a1)):
            if a1[v2] == a1[v2 - 1]:
                v1[a1[v2] + 1] = v1[a1[v2]] + 1
            elif a1[v2] == a1[v2 - 1] + 1:
                v1[a1[v2] + 1] = v1[a1[v2]] + 1
                v1[a1[v2]] = v1[a1[v2] - 1] + 1
            elif a1[v2] == a1[v2 - 1] + 2:
                v1[a1[v2]] = v1[a1[v2] - 1] + 1
                v1[a1[v2] + 1] = 1
            else:
                v1[a1[v2]] = v1[a1[v2] + 1] = 1
        return max(v1.values())

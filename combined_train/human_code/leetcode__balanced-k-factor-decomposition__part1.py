import bisect

def f1(a1):
    v1 = [[] for v2 in range(a1 + 1)]
    for v3 in range(1, a1 + 1):
        for v4 in range(v3, a1 + 1, v3):
            v1[v4].append(v3)
    return v1
v1 = 10 ** 5
v2 = f1(v1)

class C1(object):

    def minDifference(self, a1, a2):
        """
        """

        def backtracking(a1):
            v1 = curr[-1] if curr else 1
            if len(curr) == a2 - 1 and a1 >= v1:
                curr.append(a1)
                if not result or result[-1] - result[0] > curr[-1] - curr[0]:
                    result[:] = curr
                curr.pop()
                return
            v2 = v2[a1]
            for v3 in range(bisect.bisect_left(v2, v1), len(v2)):
                curr.append(v2[v3])
                backtracking(a1 // v2[v3])
                curr.pop()
        v1, v2 = ([], [])
        backtracking(a1)
        return v1

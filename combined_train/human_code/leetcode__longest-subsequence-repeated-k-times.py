import collections

class C1(object):

    def longestSubsequenceRepeatedK(self, a1, a2):
        """
        """

        def check(a1, a2, a3):
            if not a3:
                return True
            v1 = 0
            for v2 in a1:
                if v2 != a3[v1]:
                    continue
                v1 += 1
                if v1 != len(a3):
                    continue
                v1 = 0
                a2 -= 1
                if not a2:
                    return True
            return False

        def backtracking(a1, a2, a3, a4, a5):
            if not check(a1, a2, a3):
                return
            if len(a3) > len(a5):
                a5[:] = a3
            for v1 in reversed(string.ascii_lowercase):
                if a4[v1] < a2:
                    continue
                a4[v1] -= a2
                a3.append(v1)
                backtracking(a1, a2, a3, a4, a5)
                a3.pop()
                a4[v1] += a2
        v1 = collections.Counter(a1)
        v2 = []
        for v3 in a1:
            if v1[v3] < a2:
                continue
            v2.append(v3)
        v4 = []
        backtracking(v2, a2, [], v1, v4)
        return ''.join(v4)

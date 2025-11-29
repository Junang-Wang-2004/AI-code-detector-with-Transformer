import collections

class C1(object):

    def smallestSubsequence(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2, v3 = (set(), [])
        for v4 in a1:
            if v4 not in v2:
                while v3 and v3[-1] > v4 and v1[v3[-1]]:
                    v2.remove(v3.pop())
                v3 += v4
                v2.add(v4)
            v1[v4] -= 1
        return ''.join(v3)

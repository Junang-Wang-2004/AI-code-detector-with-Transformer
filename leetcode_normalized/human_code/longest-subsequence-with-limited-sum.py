import bisect

class C1(object):

    def answerQueries(self, a1, a2):
        """
        """
        a1.sort()
        for v1 in range(len(a1) - 1):
            a1[v1 + 1] += a1[v1]
        return [bisect.bisect_right(a1, q) for v2 in a2]

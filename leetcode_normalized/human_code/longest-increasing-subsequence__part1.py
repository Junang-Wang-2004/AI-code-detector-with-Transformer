import bisect

class C1(object):

    def lengthOfLIS(self, a1):
        """
        """
        v1 = []

        def insert(a1):
            v1 = bisect.bisect_left(v1, a1)
            if v1 == len(v1):
                v1.append(a1)
            else:
                v1[v1] = a1
        for v2 in a1:
            insert(v2)
        return len(v1)

import itertools
import re

class C1(object):

    def summaryRanges(self, a1):
        v1 = []
        if not a1:
            return v1
        v2, v3 = (a1[0], a1[0])
        for v4 in range(1, len(a1) + 1):
            if v4 < len(a1) and a1[v4] == v3 + 1:
                v3 = a1[v4]
            else:
                v5 = str(v2)
                if v2 != v3:
                    v5 += '->' + str(v3)
                v1.append(v5)
                if v4 < len(a1):
                    v2 = v3 = a1[v4]
        return v1

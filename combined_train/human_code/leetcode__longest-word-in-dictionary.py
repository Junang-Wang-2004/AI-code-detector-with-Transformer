from collections import defaultdict
from operator import getitem

class C1(object):

    def longestWord(self, a1):
        """
        """
        v1 = lambda: defaultdict(v1)
        v2 = v1()
        for v3, v4 in enumerate(a1):
            reduce(getitem, v4, v2)['_end'] = v3
        v5 = list(v2.values())
        v6 = ''
        while v5:
            v7 = v5.pop()
            if '_end' in v7:
                v4 = a1[v7['_end']]
                if len(v4) > len(v6) or (len(v4) == len(v6) and v4 < v6):
                    v6 = v4
                v5 += [v7[letter] for v8 in v7 if v8 != '_end']
        return v6

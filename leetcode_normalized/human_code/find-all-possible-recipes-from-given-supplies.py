import collections
import itertools

class C1(object):

    def findAllRecipes(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = collections.defaultdict(list)
        for v3, v4 in zip(a1, a2):
            v1[v3] = len(v4)
            for v5 in v4:
                v2[v5].append(v3)
        v6 = []
        a1 = set(a1)
        v8 = a3
        while v8:
            v9 = []
            for v10 in v8:
                if v10 in a1:
                    v6.append(v10)
                for v11 in v2[v10]:
                    v1[v11] -= 1
                    if not v1[v11]:
                        v9.append(v11)
            v8 = v9
        return v6

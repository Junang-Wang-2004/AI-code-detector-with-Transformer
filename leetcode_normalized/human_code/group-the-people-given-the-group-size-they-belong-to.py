import collections

class C1(object):

    def groupThePeople(self, a1):
        """
        """
        v1, v2 = (collections.defaultdict(list), [])
        for v3, v4 in enumerate(a1):
            v1[v4].append(v3)
            if len(v1[v4]) == v4:
                v2.append(v1.pop(v4))
        return v2

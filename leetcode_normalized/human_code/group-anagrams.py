import collections

class C1(object):

    def groupAnagrams(self, a1):
        """
        """
        v1, v2 = (collections.defaultdict(list), [])
        for v3 in a1:
            v4 = ''.join(sorted(v3))
            v1[v4].append(v3)
        for v5 in list(v1.values()):
            v5.sort()
            v2.append(v5)
        return v2

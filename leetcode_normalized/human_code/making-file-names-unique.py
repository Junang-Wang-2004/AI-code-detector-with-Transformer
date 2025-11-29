import collections

class C1(object):

    def getFolderNames(self, a1):
        """
        """
        v1 = collections.Counter()
        v2, v3 = ([], set())
        for v4 in a1:
            while True:
                v5 = '{}({})'.format(v4, v1[v4]) if v1[v4] else v4
                v1[v4] += 1
                if v5 not in v3:
                    break
            v2.append(v5)
            v3.add(v5)
        return v2

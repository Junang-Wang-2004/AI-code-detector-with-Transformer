import collections

class C1(object):

    def findDuplicate(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2 in a1:
            v3 = v2.split(' ')
            for v4 in range(1, len(v3)):
                v5 = v3[0] + '/' + v3[v4][0:v3[v4].find('(')]
                v6 = v3[v4][v3[v4].find('(') + 1:v3[v4].find(')')]
                v1[v6].append(v5)
        v7 = []
        for v6, v8 in v1.items():
            if len(v8) > 1:
                v7.append(v8)
        return v7

class C1(object):

    def __init__(self):
        self.__root = {}

    def insert(self, a1):
        v1 = self.__root
        for v2 in reversed(range(32)):
            v3 = a1 >> v2 & 1
            if v3 not in v1:
                v1[v3] = {'_count': 0}
            v1 = v1[v3]
            v1['_count'] += 1

    def query(self, a1, a2):
        v1, v2 = (self.__root, 0)
        for v3 in reversed(range(32)):
            v4 = a1 >> v3 & 1
            v5 = a2 >> v3 & 1
            if v5:
                if v4 in v1:
                    v2 += v1[0 ^ v4]['_count']
            if v5 ^ v4 not in v1:
                break
            v1 = v1[v5 ^ v4]
        return v2

class C2(object):

    def countPairs(self, a1, a2, a3):
        """
        """
        v1 = 0
        v2 = C1()
        for v3 in a1:
            v1 += v2.query(v3, a3 + 1) - v2.query(v3, a2)
            v2.insert(v3)
        return v1

import collections

class C1(object):

    def getWidth(self, a1, a2):
        """
        """
        pass

    def getHeight(self, a1):
        """
        """
        pass

class C2(object):

    def maxFont(self, a1, a2, a3, a4, a5):
        """
        """

        def check(a1, a2, a3, a4, a5, a6):
            return a5.getHeight(a4[a6]) <= a3 and sum((cnt * a5.getWidth(a4[a6], c) for v1, v2 in a1.items())) <= a2
        v1 = collections.Counter(a1)
        v2, v3 = (0, len(a4) - 1)
        while v2 <= v3:
            v4 = v2 + (v3 - v2) // 2
            if not check(v1, a2, a3, a4, a5, v4):
                v3 = v4 - 1
            else:
                v2 = v4 + 1
        return a4[v3] if v3 >= 0 else -1

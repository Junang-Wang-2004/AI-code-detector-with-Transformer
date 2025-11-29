class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * (a1 + 1)

    def add(self, a1, a2):
        a1 += 1
        while a1 < len(self.__bit):
            self.__bit[a1] += a2
            a1 += a1 & -a1

    def query(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 += self.__bit[a1]
            a1 -= a1 & -a1
        return v2

class C2(object):

    def minMovesToMakePalindrome(self, a1):
        """
        """
        v1 = [[] for v2 in range(26)]
        for v3, v4 in enumerate(a1):
            v1[ord(v4) - ord('a')].append(v3)
        v5, v6 = ([0] * len(a1), [])
        for v4, v7 in enumerate(v1):
            for v3 in range(len(v7) // 2):
                v6.append((v7[v3], v7[~v3]))
            if len(v7) % 2:
                v5[v7[len(v7) // 2]] = len(a1) // 2
        v6.sort()
        for v3, (v8, v9) in enumerate(v6):
            v5[v8], v5[v9] = (v3, len(a1) - 1 - v3)
        v10 = C1(len(a1))
        v11 = 0
        for v3 in v5:
            v11 += v3 - v10.query(v3 - 1)
            v10.add(v3, 1)
        return v11

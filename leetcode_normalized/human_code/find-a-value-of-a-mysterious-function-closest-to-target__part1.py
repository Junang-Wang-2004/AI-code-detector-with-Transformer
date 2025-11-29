class C1(object):

    def __init__(self, a1):
        self.__l = 0
        self.__n = a1
        self.__count = [0] * a1

    def __iadd__(self, a1):
        self.__l += 1
        v1 = 1
        for v2 in range(self.__n):
            if a1 & v1:
                self.__count[v2] += 1
            v1 <<= 1
        return self

    def __isub__(self, a1):
        self.__l -= 1
        v1 = 1
        for v2 in range(self.__n):
            if a1 & v1:
                self.__count[v2] -= 1
            v1 <<= 1
        return self

    def bit_and(self):
        v1, v2 = (0, 1)
        for v3 in range(self.__n):
            if self.__count[v3] == self.__l:
                v1 |= v2
            v2 <<= 1
        return v1

class C2(object):

    def closestToTarget(self, a1, a2):
        """
        """
        v1 = C1(max(a1).bit_length())
        v2, v3 = (float('inf'), 0)
        for v4 in range(len(a1)):
            v1 += a1[v4]
            while v3 <= v4:
                v5 = v1.bit_and()
                v2 = min(v2, abs(v5 - a2))
                if v5 >= a2:
                    break
                v1 -= a1[v3]
                v3 += 1
        return v2

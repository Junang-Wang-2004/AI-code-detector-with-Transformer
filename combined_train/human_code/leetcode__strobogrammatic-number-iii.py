class C1(object):
    v1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    v2 = {}

    def strobogrammaticInRange(self, a1, a2):
        v1 = self.countStrobogrammaticUntil(a2, False) - self.countStrobogrammaticUntil(a1, False) + self.isStrobogrammatic(a1)
        return v1 if v1 >= 0 else 0

    def countStrobogrammaticUntil(self, a1, a2):
        if a2 and a1 in self.cache:
            return self.cache[a1]
        v1 = 0
        if len(a1) == 1:
            for v2 in ['0', '1', '8']:
                if a1[0] >= v2:
                    v1 += 1
            self.cache[a1] = v1
            return v1
        for v3, v4 in self.lookup.items():
            if a2 or v3 != '0':
                if a1[0] > v3:
                    if len(a1) == 2:
                        v1 += 1
                    else:
                        v1 += self.countStrobogrammaticUntil('9' * (len(a1) - 2), True)
                elif a1[0] == v3:
                    if len(a1) == 2:
                        if a1[-1] >= v4:
                            v1 += 1
                    elif a1[-1] >= v4:
                        v1 += self.countStrobogrammaticUntil(self.getMid(a1), True)
                    elif self.getMid(a1) != '0' * (len(a1) - 2):
                        v1 += self.countStrobogrammaticUntil(self.getMid(a1), True) - self.isStrobogrammatic(self.getMid(a1))
        if not a2:
            for v5 in range(len(a1) - 1, 0, -1):
                v1 += self.countStrobogrammaticByLength(v5)
        else:
            self.cache[a1] = v1
        return v1

    def getMid(self, a1):
        return a1[1:len(a1) - 1]

    def countStrobogrammaticByLength(self, a1):
        if a1 == 1:
            return 3
        elif a1 == 2:
            return 4
        elif a1 == 3:
            return 4 * 3
        else:
            return 5 * self.countStrobogrammaticByLength(a1 - 2)

    def isStrobogrammatic(self, a1):
        v1 = len(a1)
        for v2 in range((v1 + 1) / 2):
            if a1[v1 - 1 - v2] not in self.lookup or a1[v2] != self.lookup[a1[v1 - 1 - v2]]:
                return False
        return True

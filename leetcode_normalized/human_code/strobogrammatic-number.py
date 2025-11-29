class C1(object):
    v1 = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    def isStrobogrammatic(self, a1):
        v1 = len(a1)
        for v2 in range((v1 + 1) / 2):
            if a1[v1 - 1 - v2] not in self.lookup or a1[v2] != self.lookup[a1[v1 - 1 - v2]]:
                return False
        return True

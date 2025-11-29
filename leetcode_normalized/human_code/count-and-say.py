class C1(object):

    def countAndSay(self, a1):
        v1 = '1'
        for v2 in range(a1 - 1):
            v1 = self.getNext(v1)
        return v1

    def getNext(self, a1):
        v1, v2 = (0, '')
        while v1 < len(a1):
            v3 = 1
            while v1 < len(a1) - 1 and a1[v1] == a1[v1 + 1]:
                v3 += 1
                v1 += 1
            v2 += str(v3) + a1[v1]
            v1 += 1
        return v2

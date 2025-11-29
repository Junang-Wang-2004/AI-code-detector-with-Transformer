class C1(object):

    def getCommon(self, a1, a2):
        v1 = 0
        v2 = 0
        while True:
            if v1 >= len(a1) or v2 >= len(a2):
                return -1
            if a1[v1] == a2[v2]:
                return a1[v1]
            if a1[v1] < a2[v2]:
                v1 += 1
            else:
                v2 += 1

class C1(object):

    def depthSum(self, a1):
        v1 = [(a1, 1)]
        v2 = 0
        while v1:
            v3, v4 = v1.pop()
            for v5 in v3:
                if v5.isInteger():
                    v2 += v5.getInteger() * v4
                else:
                    v1.append((v5.getList(), v4 + 1))
        return v2

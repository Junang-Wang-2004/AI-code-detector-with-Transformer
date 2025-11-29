class C1:

    def maxDepthAfterSplit(self, a1):
        v1 = []
        v2 = 0
        for v3 in a1:
            if v3 == '(':
                v1.append(v2 % 2)
                v2 += 1
            else:
                v2 -= 1
                v1.append(v2 % 2)
        return v1

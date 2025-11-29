class C1(object):

    def averageOfLevels(self, a1):
        """
        """
        v1 = []
        v2 = [a1]
        while v2:
            v3, v4 = (0, 0)
            v5 = []
            for v6 in v2:
                v3 += v6.val
                v4 += 1
                if v6.left:
                    v5.append(v6.left)
                if v6.right:
                    v5.append(v6.right)
            v2 = v5
            v1.append(float(v3) / v4)
        return v1

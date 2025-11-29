class C1(object):

    def minimumLevel(self, a1):
        v1 = []
        v2 = [a1]
        v3 = 1
        while v2:
            v4 = []
            v5 = 0
            for v6 in v2:
                v5 += v6.val
                if v6.left:
                    v4.append(v6.left)
                if v6.right:
                    v4.append(v6.right)
            v1.append((v5, v3))
            v2 = v4
            v3 += 1
        return min(v1)[-1]

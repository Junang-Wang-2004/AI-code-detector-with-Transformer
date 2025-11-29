class C1(object):

    def checkEqualTree(self, a1):
        v1 = set()
        v2 = [0]

        def dfs(a1):
            if not a1:
                return 0
            v1 = dfs(a1.left)
            v2 = dfs(a1.right)
            v3 = a1.val + v1 + v2
            if v3 != 0:
                v1.add(v3)
            else:
                v2[0] += 1
            return v3
        v3 = dfs(a1)
        if v3 == 0:
            return v2[0] > 1
        return v3 % 2 == 0 and v3 // 2 in v1

class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxSumBST(self, a1):
        """
        """
        v1 = 0
        v2 = [[a1, None, []]]
        while v2:
            v3, v4, v5 = v2.pop()
            if v4:
                v6, v7, v8, v9 = v4[0]
                v10, v11, v12, v13 = v4[1]
                if v6 and v10 and (v9 < v3.val < v12):
                    v14 = v7 + v3.val + v11
                    v1 = max(v1, v14)
                    v5[:] = [True, v14, min(v8, v3.val), max(v3.val, v13)]
                    continue
                v5[:] = [False, 0, 0, 0]
                continue
            if not v3:
                v5[:] = [True, 0, float('inf'), float('-inf')]
                continue
            v15 = [[], []]
            v2.append([v3, v15, v5])
            v2.append([v3.right, None, v15[1]])
            v2.append([v3.left, None, v15[0]])
        return v1

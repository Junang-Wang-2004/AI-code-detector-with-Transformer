class C1(object):

    def maxLevelSum(self, a1):
        """
        """
        v1, v2, v3 = (0, 1, float('-inf'))
        v4 = collections.deque([a1])
        while v4:
            v5 = 0
            for v6 in range(len(v4)):
                v7 = v4.popleft()
                v5 += v7.val
                if v7.left:
                    v4.append(v7.left)
                if v7.right:
                    v4.append(v7.right)
            if v5 > v3:
                v1, v3 = (v2, v5)
            v2 += 1
        return v1

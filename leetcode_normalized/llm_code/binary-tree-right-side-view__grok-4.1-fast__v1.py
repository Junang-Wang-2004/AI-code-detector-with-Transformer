class C1:

    def rightSideView(self, a1):
        if not a1:
            return []
        v1 = []
        v2 = [(a1, 0)]
        v3 = -1
        while v2:
            v4, v5 = v2.pop()
            if v5 > v3:
                v1.append(v4.val)
                v3 = v5
            if v4.left:
                v2.append((v4.left, v5 + 1))
            if v4.right:
                v2.append((v4.right, v5 + 1))
        return v1

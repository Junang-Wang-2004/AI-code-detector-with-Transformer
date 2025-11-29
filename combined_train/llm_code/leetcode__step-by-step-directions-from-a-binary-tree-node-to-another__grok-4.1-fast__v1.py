class C1(object):

    def getDirections(self, a1, a2, a3):

        def find_path(a1, a2):
            if not a1:
                return None
            if a1.val == a2:
                return [a1]
            v1 = find_path(a1.left, a2)
            if v1 is not None:
                return [a1] + v1
            v2 = find_path(a1.right, a2)
            if v2 is not None:
                return [a1] + v2
            return None
        v1 = find_path(a1, a2)
        v2 = find_path(a1, a3)
        v3 = 0
        v4 = min(len(v1), len(v2))
        while v3 < v4 and v1[v3] == v2[v3]:
            v3 += 1
        v5 = 'U' * (len(v1) - v3)
        for v6 in range(v3, len(v2) - 1):
            if v2[v6 + 1] == v2[v6].left:
                v5 += 'L'
            else:
                v5 += 'R'
        return v5

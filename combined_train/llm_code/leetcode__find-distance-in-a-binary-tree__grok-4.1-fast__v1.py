class C1(object):

    def findDistance(self, a1, a2, a3):

        def get_path(a1, a2):
            if not a1:
                return []
            v1 = [(a1, [a1])]
            while v1:
                v2, v3 = v1.pop()
                if v2.val == a2:
                    return v3
                for v4 in (v2.right, v2.left):
                    if v4:
                        v1.append((v4, v3 + [v4]))
            return []
        v1 = get_path(a1, a2)
        v2 = get_path(a1, a3)
        v3 = 0
        v4 = min(len(v1), len(v2))
        while v3 < v4 and v1[v3] == v2[v3]:
            v3 += 1
        return len(v1) - v3 + len(v2) - v3

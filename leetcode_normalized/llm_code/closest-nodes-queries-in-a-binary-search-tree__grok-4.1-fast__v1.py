class C1(object):

    def closestNodes(self, a1, a2):

        def find_floor_ceiling(a1, a2):
            v1 = -1
            v2 = -1
            v3 = a1
            while v3:
                if v3.val == a2:
                    return [a2, a2]
                if v3.val < a2:
                    v1 = v3.val
                    v3 = v3.right
                else:
                    v2 = v3.val
                    v3 = v3.left
            return [v1, v2]
        return [find_floor_ceiling(a1, q) for v1 in a2]

class C1:

    def findLeaves(self, a1):
        if not a1:
            return []
        v1 = {}

        def get_height(a1):
            if a1 is None:
                return -1
            if a1 in v1:
                return v1[a1]
            v1 = get_height(a1.left)
            v2 = get_height(a1.right)
            v1[a1] = 1 + max(v1, v2)
            return v1[a1]
        get_height(a1)
        v2 = v1[a1]
        v3 = [[] for v4 in range(v2 + 1)]

        def assign(a1):
            if a1 is None:
                return
            assign(a1.left)
            assign(a1.right)
            v3[v1[a1]].append(a1.val)
        assign(a1)
        return v3

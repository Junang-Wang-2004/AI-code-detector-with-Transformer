class C1(object):

    def closestMeetingNode(self, a1, a2, a3):
        """
        """

        def dfs(a1):
            v1 = {}
            v2 = 0
            while a1 != -1:
                if a1 in v1:
                    break
                v1[a1] = v2
                v2 += 1
                a1 = a1[a1]
            return v1
        v1, v2 = (dfs(a2), dfs(a3))
        v3 = set(v1.keys()) & set(v2.keys())
        return min(v3, key=lambda x: (max(v1[x], v2[x]), x)) if v3 else -1

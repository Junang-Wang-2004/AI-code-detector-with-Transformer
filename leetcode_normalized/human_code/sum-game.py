class C1(object):

    def sumGame(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] == '?':
                v1 += -1 if v3 < len(a1) // 2 else 1
            else:
                v2 += int(a1[v3]) if v3 < len(a1) // 2 else -int(a1[v3])
        return True if v1 % 2 else v2 != v1 // 2 * 9

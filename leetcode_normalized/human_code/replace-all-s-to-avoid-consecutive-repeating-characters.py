class C1(object):

    def modifyString(self, a1):
        """
        """
        a1 = list(a1)
        for v2 in range(len(a1)):
            if a1[v2] != '?':
                continue
            for v3 in ('a', 'b', 'c'):
                if (v2 == 0 or a1[v2 - 1] != v3) and (v2 == len(a1) - 1 or v3 != a1[v2 + 1]):
                    break
            a1[v2] = v3
        return ''.join(a1)

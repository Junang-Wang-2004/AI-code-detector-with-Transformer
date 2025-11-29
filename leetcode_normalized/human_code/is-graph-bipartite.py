class C1(object):

    def isBipartite(self, a1):
        """
        """
        v1 = {}
        for v2 in range(len(a1)):
            if v2 in v1:
                continue
            v3 = [v2]
            v1[v2] = 0
            while v3:
                v4 = v3.pop()
                for v5 in a1[v4]:
                    if v5 not in v1:
                        v3.append(v5)
                        v1[v5] = v1[v4] ^ 1
                    elif v1[v5] == v1[v4]:
                        return False
        return True

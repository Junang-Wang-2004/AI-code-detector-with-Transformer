class C1(object):

    def canBeValid(self, a1, a2):
        """
        """
        if len(a1) % 2:
            return False
        for v1, v2 in ((lambda x: x, '('), (reversed, ')')):
            v3 = v4 = 0
            for v5 in v1(range(len(a1))):
                if a2[v5] == '0':
                    v3 += 1
                else:
                    v4 += 1 if a1[v5] == v2 else -1
                    if v3 + v4 < 0:
                        return False
        return True

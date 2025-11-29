class C1(object):

    def removeComments(self, a1):
        """
        """
        v1 = False
        v2, v3 = ([], [])
        for v4 in a1:
            v5 = 0
            while v5 < len(v4):
                if not v1 and v5 + 1 < len(v4) and (v4[v5:v5 + 2] == '/*'):
                    v1 = True
                    v5 += 1
                elif v1 and v5 + 1 < len(v4) and (v4[v5:v5 + 2] == '*/'):
                    v1 = False
                    v5 += 1
                elif not v1 and v5 + 1 < len(v4) and (v4[v5:v5 + 2] == '//'):
                    break
                elif not v1:
                    v3.append(v4[v5])
                v5 += 1
            if v3 and (not v1):
                v2.append(''.join(v3))
                v3 = []
        return v2

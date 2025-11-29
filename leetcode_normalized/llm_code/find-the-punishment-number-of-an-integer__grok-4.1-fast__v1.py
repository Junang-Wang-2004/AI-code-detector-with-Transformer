class C1(object):

    def punishmentNumber(self, a1):

        def valid_split(a1, a2):
            v1 = len(a1)

            def explore(a1, a2):
                if a1 == v1:
                    return a2 == 0
                for v1 in range(a1 + 1, v1 + 1):
                    v2 = a1[a1:v1]
                    if len(v2) > 1 and v2[0] == '0':
                        continue
                    v3 = int(v2)
                    if v3 > a2:
                        break
                    if explore(v1, a2 - v3):
                        return True
                return False
            return explore(0, a2)
        v1 = 0
        for v2 in range(1, a1 + 1):
            v3 = str(v2 * v2)
            if valid_split(v3, v2):
                v1 += v2 * v2
        return v1

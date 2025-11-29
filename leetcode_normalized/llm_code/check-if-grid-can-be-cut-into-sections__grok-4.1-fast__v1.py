class C1(object):

    def checkValidCuts(self, a1, a2):

        def num_groups(a1):
            if not a1:
                return 0
            a1.sort(key=lambda t: t[0])
            v1 = 1
            v2 = a1[0][1]
            for v3, v4 in a1[1:]:
                if v3 >= v2:
                    v1 += 1
                    v2 = v4
                else:
                    v2 = max(v2, v4)
            return v1
        v1 = [(rec[0], rec[2]) for v2 in a2]
        v3 = [(v2[1], v2[3]) for v2 in a2]
        return num_groups(v1) >= 3 or num_groups(v3) >= 3

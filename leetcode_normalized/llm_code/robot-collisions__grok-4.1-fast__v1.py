class C1(object):

    def survivedRobotsHealths(self, a1, a2, a3):
        v1 = len(a1)
        v2 = sorted(range(v1), key=a1.__getitem__)
        v3 = []
        for v4 in v2:
            if a3[v4] == 'R':
                v3.append(v4)
                continue
            while v3:
                v5 = v3.pop()
                v6 = a2[v5]
                v7 = a2[v4]
                if v6 > v7:
                    a2[v5] = v6 - 1
                    v3.append(v5)
                    a2[v4] = 0
                    break
                if v6 < v7:
                    a2[v5] = 0
                    a2[v4] = v7 - 1
                else:
                    a2[v5] = 0
                    a2[v4] = 0
                    break
        return [hp for v8 in a2 if v8 > 0]

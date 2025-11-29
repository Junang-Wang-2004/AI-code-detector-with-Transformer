class C1(object):

    def countMentions(self, a1, a2):
        """
        """
        v1 = [0] * a1
        v2 = [1] * a1
        a2.sort(key=lambda x: (int(x[1]), x[0] == 'MESSAGE'))
        for v3, v4, v5 in a2:
            if v3 == 'OFFLINE':
                v2[int(v5)] = int(v4) + 60
                continue
            if v5 == 'ALL':
                for v6 in range(len(v2)):
                    v1[v6] += 1
            elif v5 == 'HERE':
                for v6 in range(len(v2)):
                    if v2[v6] <= int(v4):
                        v1[v6] += 1
            else:
                for v7 in v5.split():
                    v1[int(v7[2:])] += 1
        return v1

class C1(object):

    def exclusiveTime(self, a1, a2):
        """
        """
        v1 = [0] * a1
        v2, v3 = ([], 0)
        for v4 in a2:
            v5 = v4.split(':')
            if v5[1] == 'start':
                if v2:
                    v1[v2[-1]] += int(v5[2]) - v3
                v2.append(int(v5[0]))
                v3 = int(v5[2])
            else:
                v1[v2.pop()] += int(v5[2]) - v3 + 1
                v3 = int(v5[2]) + 1
        return v1

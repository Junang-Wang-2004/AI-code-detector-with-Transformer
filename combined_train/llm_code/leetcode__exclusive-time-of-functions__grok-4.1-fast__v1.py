class C1:

    def exclusiveTime(self, a1, a2):
        v1 = [0] * a1
        v2 = []
        v3 = 0
        for v4 in a2:
            v5 = v4.split(':')
            v6 = int(v5[0])
            v7 = v5[1]
            v8 = int(v5[2])
            v9 = v8 - v3
            if v2:
                v1[v2[-1]] += v9
                if v7 == 'end':
                    v1[v2[-1]] += 1
                    v2.pop()
            if v7 == 'start':
                v2.append(v6)
            v3 = v8 if v7 == 'start' else v8 + 1
        return v1

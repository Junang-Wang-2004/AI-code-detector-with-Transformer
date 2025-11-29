class C1(object):

    def survivedRobotsHealths(self, a1, a2, a3):
        """
        """
        v1 = []
        for v2 in sorted(range(len(a1)), key=lambda x: a1[x]):
            if a3[v2] == 'R':
                v1.append(v2)
                continue
            while v1:
                if a2[v1[-1]] == a2[v2]:
                    a2[v1.pop()] = a2[v2] = 0
                    break
                if a2[v1[-1]] > a2[v2]:
                    a2[v2] = 0
                    a2[v1[-1]] -= 1
                    break
                a2[v1.pop()] = 0
                a2[v2] -= 1
        return [x for v3 in a2 if v3]

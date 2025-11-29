class C1(object):

    def maximumRequests(self, a1, a2):
        self.best = 0
        v1 = [0] * a1

        def search(a1, a2, a3):
            v1 = len(a2) - a1
            if a2 + v1 <= self.best:
                return
            if max(map(abs, a3)) > v1:
                return
            if a1 == len(a2):
                if all((d == 0 for v2 in a3)):
                    self.best = a2
                return
            v3, v4 = a2[a1]
            a3[v3] -= 1
            a3[v4] += 1
            search(a1 + 1, a2 + 1, a3)
            a3[v3] += 1
            a3[v4] -= 1
            search(a1 + 1, a2, a3)
        search(0, 0, v1)
        return self.best

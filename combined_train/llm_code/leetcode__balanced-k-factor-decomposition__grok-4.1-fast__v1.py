import bisect

class C1:

    def minDifference(self, a1, a2):
        self.best_path = []
        self.min_range = float('inf')

        def get_divisors(a1):
            v1 = []
            v2 = 1
            while v2 * v2 <= a1:
                if a1 % v2 == 0:
                    v1.append(v2)
                    if v2 != a1 // v2:
                        v1.append(a1 // v2)
                v2 += 1
            v1.sort()
            return v1

        def search(a1, a2, a3, a4):
            if a2 == a2:
                if a1 == 1:
                    v1 = a4[-1] - a4[0]
                    if v1 < self.min_range:
                        self.min_range = v1
                        self.best_path = a4[:]
                return
            if a4 and a4[-1] - a4[0] >= self.min_range:
                return
            v2 = get_divisors(a1)
            v3 = bisect.bisect_left(v2, a3)
            for v4 in range(len(v2) - 1, v3 - 1, -1):
                v5 = v2[v4]
                a4.append(v5)
                search(a1 // v5, a2 + 1, v5, a4)
                a4.pop()
        search(a1, 0, 1, [])
        return self.best_path

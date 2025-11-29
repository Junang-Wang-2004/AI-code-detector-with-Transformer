class C1:

    def distributeCandies(self, a1, a2):

        def count_ways(a1):
            if a1 < 0:
                return 0
            return (a1 + 2) * (a1 + 1) // 2
        v1 = a2 + 1
        v2 = count_ways(a1)
        v2 -= 3 * count_ways(a1 - v1)
        v2 += 3 * count_ways(a1 - 2 * v1)
        v2 -= count_ways(a1 - 3 * v1)
        return v2

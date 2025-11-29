class C1(object):

    def findProductsOfElements(self, a1):

        def ones_up_to(a1):
            if a1 < 0:
                return 0
            v1 = 0
            v2 = 0
            while 1 << v2 <= a1:
                v3 = 1 << v2 + 1
                v4 = (a1 + 1) // v3
                v1 += v4 * (v3 // 2)
                v5 = (a1 + 1) % v3
                if v5 > 1 << v2:
                    v1 += v5 - (1 << v2)
                v2 += 1
            return v1

        def sum_pos_up_to(a1):
            if a1 < 0:
                return 0
            v1 = 0
            v2 = 0
            while 1 << v2 <= a1:
                v3 = 1 << v2 + 1
                v4 = (a1 + 1) // v3
                v5 = v4 * (v3 // 2)
                v6 = (a1 + 1) % v3
                if v6 > 1 << v2:
                    v5 += v6 - (1 << v2)
                v1 += v2 * v5
                v2 += 1
            return v1

        def find_smallest_y(a1):
            v1 = 0
            v2 = a1
            while v1 < v2:
                v3 = v1 + (v2 - v1) // 2
                if ones_up_to(v3) >= a1:
                    v2 = v3
                else:
                    v1 = v3 + 1
            return v1

        def total_pos_sum(a1):
            if a1 == 0:
                return 0
            v1 = find_smallest_y(a1)
            v2 = ones_up_to(v1 - 1)
            v3 = sum_pos_up_to(v1 - 1)
            v4 = a1 - v2
            v5 = 0
            v6 = 0
            v7 = v1
            while v4 > 0 and 1 << v6 <= v7:
                if v7 & 1 << v6:
                    v5 += v6
                    v4 -= 1
                v6 += 1
            return v3 + v5
        return [pow(2, total_pos_sum(r + 1) - total_pos_sum(l), m) for v1, v2, v3 in a1]

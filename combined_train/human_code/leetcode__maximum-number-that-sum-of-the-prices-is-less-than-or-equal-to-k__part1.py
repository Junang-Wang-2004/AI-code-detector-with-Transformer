class C1(object):

    def findMaximumNumber(self, a1, a2):
        """
        """

        def floor_log2(a1):
            return a1.bit_length() - 1

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def count(a1):
            return (prefix_cnt << a2 * a1) + lookup[a1]
        v1 = v2 = 0
        v3 = [0]
        v4 = 0
        while (v3[-1] << a2) + (1 << v4 + a2 - 1) <= a1:
            v3.append((v3[-1] << a2) + (1 << v4 + a2 - 1))
            v4 += a2
        while a1 >= v2:
            v5 = binary_search_right(1, len(v3) - 1, lambda l: count(v5) <= a1)
            v6, v4 = (count(v5), a2 * v5)
            v7 = min(floor_log2(a1 // v6) if v6 else float('inf'), a2 - 1)
            v6 <<= v7
            v4 += v7
            a1 -= v6
            v1 += 1 << v4
            v2 += int((v4 + 1) % a2 == 0)
        return v1 - 1

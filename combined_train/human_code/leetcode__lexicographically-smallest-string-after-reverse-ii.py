class C1(object):

    def lexSmallest(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 29

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def get_prefix_hash(a1, a2):
            return (prefix[a2 + 1] - prefix[a1] * base[a2 - a1 + 1]) % v1 if a1 <= a2 else 0

        def get_suffix_hash(a1, a2):
            return (suffix[a1] - suffix[a2 + 1] * base[a2 - a1 + 1]) % v1 if a1 <= a2 else 0

        def get_total_hash(a1, a2, a3):
            if not a2:
                return get_suffix_hash(a1 - a3, a1 - 1) if a3 <= a1 else (get_suffix_hash(0, a1 - 1) * base[a3 - a1] + get_prefix_hash(a1, a3 - 1)) % v1
            v1 = len(a1) - a1
            return get_prefix_hash(0, a3 - 1) if a3 <= v1 else (get_prefix_hash(0, v1 - 1) * base[a3 - v1] + get_suffix_hash(len(a1) - (a3 - v1), len(a1) - 1)) % v1

        def get_char(a1, a2, a3):
            if not a2:
                return a1[a1 - 1 - a3] if a3 < a1 else a1[a3]
            return a1[a3] if a3 < len(a1) - a1 else a1[len(a1) - 1 - (a3 - (len(a1) - a1))]

        def is_less(a1, a2):
            v1 = binary_search(0, len(a1) - 1, lambda x: get_total_hash(a1, a2, x + 1) != get_total_hash(best_k, best_i, x + 1))
            return v1 != len(a1) and get_char(a1, a2, v1) < get_char(best_k, best_i, v1)
        v3 = [0] * (len(a1) + 1)
        for v4 in range(len(v3) - 1):
            v3[v4 + 1] = (v3[v4] * v2 + ord(a1[v4])) % v1
        v5 = [0] * (len(a1) + 1)
        for v4 in reversed(range(len(v5) - 1)):
            v5[v4] = (v5[v4 + 1] * v2 + ord(a1[v4])) % v1
        v6 = [1] * (len(a1) + 1)
        for v4 in range(len(v6) - 1):
            v6[v4 + 1] = v6[v4] * v2 % v1
        v7, v8 = (1, 0)
        v9 = min(a1)
        for v10 in range(1, len(a1) + 1):
            if a1[v10 - 1] != v9:
                continue
            if is_less(v10, 0):
                v7, v8 = (v10, 0)
        for v10 in range(1, len(a1) + 1):
            if not a1[-v10] >= a1[-1]:
                continue
            if is_less(v10, 1):
                v7, v8 = (v10, 1)
        return a1[:v7][::-1] + a1[v7:] if not v8 else a1[:-v7] + a1[-v7:][::-1]

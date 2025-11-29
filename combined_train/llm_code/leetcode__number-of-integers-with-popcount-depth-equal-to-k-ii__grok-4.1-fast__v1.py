class C1(object):

    def popcountDepth(self, a1, a2):

        def pop_cnt(a1):
            return bin(a1).count('1')

        def get_depth(a1):
            v1 = 0
            v2 = a1
            while True:
                if v2 == 1:
                    return v1
                if v2 == 0:
                    return v1 + 1
                v2 = pop_cnt(v2)
                v1 += 1
        v1 = len(a1)
        v2 = 0
        v3 = 10 ** 15
        while v3 != 1:
            v3 = (v3 - 1).bit_length()
            v2 += 1

        class FenwickTree(object):

            def __init__(self, a1):
                self.capacity = a1
                self.tree_arr = [0] * (a1 + 1)

            def update(self, a1, a2):
                a1 += 1
                while a1 <= self.capacity:
                    self.tree_arr[a1] += a2
                    a1 += a1 & -a1

            def prefix_sum(self, a1):
                a1 += 1
                v2 = 0
                while a1 > 0:
                    v2 += self.tree_arr[a1]
                    a1 -= a1 & -a1
                return v2
        v4 = [FenwickTree(v1) for v5 in range(v2 + 1)]
        for v6 in range(v1):
            v7 = get_depth(a1[v6])
            v4[v7].update(v6, 1)
        v8 = []
        for v9 in a2:
            if v9[0] == 1:
                v10 = v9[1]
                v11 = v9[2]
                v12 = v9[3]
                v13 = v4[v12].prefix_sum(v11) - v4[v12].prefix_sum(v10 - 1)
                v8.append(v13)
            else:
                v6 = v9[1]
                v14 = v9[2]
                v15 = a1[v6]
                v16 = get_depth(v15)
                v17 = get_depth(v14)
                a1[v6] = v14
                if v16 != v17:
                    v4[v16].update(v6, -1)
                    v4[v17].update(v6, 1)
        return v8

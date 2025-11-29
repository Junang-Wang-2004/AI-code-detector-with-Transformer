class C1:

    def tourOfKnight(self, a1, a2, a3, a4):
        v1 = [[-1] * a2 for v2 in range(a1)]
        v1[a3][a4] = 0
        v3 = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        def get_valid_moves(a1, a2):
            v1 = []
            for v2, v3 in v3:
                v4 = a1 + v2
                v5 = a2 + v3
                if 0 <= v4 < a1 and 0 <= v5 < a2 and (v1[v4][v5] == -1):
                    v1.append((v4, v5))
            return v1

        def find_path(a1, a2, a3):
            if a3 == a1 * a2:
                return True
            v1 = get_valid_moves(a1, a2)
            v1.sort(key=lambda pos: len(get_valid_moves(pos[0], pos[1])))
            for v2, v3 in v1:
                v1[v2][v3] = a3
                if find_path(v2, v3, a3 + 1):
                    return True
                v1[v2][v3] = -1
            return False
        find_path(a3, a4, 1)
        return v1

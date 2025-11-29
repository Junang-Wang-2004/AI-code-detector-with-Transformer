class C1:

    def canIWin(self, a1, a2):
        v1 = a1
        if v1 * (v1 + 1) // 2 < a2:
            return False
        v2 = {}

        def player_can_force_win(a1, a2):
            if a2 in v2:
                return v2[a2]
            for v1 in range(v1 - 1, -1, -1):
                v2 = 1 << v1
                if a2 & v2 == 0:
                    v3 = v1 + 1
                    v4 = a1 - v3
                    v5 = a2 | v2
                    if v3 >= a1 or not player_can_force_win(v4, v5):
                        v2[a2] = True
                        return True
            v2[a2] = False
            return False
        return player_can_force_win(a2, 0)

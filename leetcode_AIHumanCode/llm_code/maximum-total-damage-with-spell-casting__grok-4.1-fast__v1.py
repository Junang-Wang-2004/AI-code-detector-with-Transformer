class Solution:
    def maximumTotalDamage(self, monster_powers):
        monster_powers.sort()
        if not monster_powers:
            return 0
        level_sums = []
        idx = 0
        n = len(monster_powers)
        while idx < n:
            curr_level = monster_powers[idx]
            level_sum = 0
            while idx < n and monster_powers[idx] == curr_level:
                level_sum += monster_powers[idx]
                idx += 1
            level_sums.append((curr_level, level_sum))
        active_windows = []
        historic_max = 0
        for level, sum_power in level_sums:
            while active_windows and active_windows[0][0] + 2 < level:
                historic_max = max(historic_max, active_windows.pop(0)[1])
            this_damage = historic_max + sum_power
            active_windows.append([level, this_damage])
        return max(dmg for _, dmg in active_windows)

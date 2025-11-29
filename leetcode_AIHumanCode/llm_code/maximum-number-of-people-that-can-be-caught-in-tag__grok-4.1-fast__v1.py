class Solution(object):
    def catchMaximumAmountofPeople(self, team, dist):
        cops = []
        suspects = []
        length = len(team)
        for pos in range(length):
            if team[pos] == 1:
                cops.append(pos)
            else:
                suspects.append(pos)
        idx_c = 0
        idx_s = 0
        count = 0
        while idx_c < len(cops) and idx_s < len(suspects):
            separation = abs(cops[idx_c] - suspects[idx_s])
            if separation <= dist:
                count += 1
                idx_c += 1
                idx_s += 1
            elif cops[idx_c] < suspects[idx_s]:
                idx_c += 1
            else:
                idx_s += 1
        return count

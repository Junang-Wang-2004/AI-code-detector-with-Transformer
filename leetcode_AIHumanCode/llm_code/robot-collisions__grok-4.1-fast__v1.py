class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        order = sorted(range(n), key=positions.__getitem__)
        survivors = []
        for i in order:
            if directions[i] == 'R':
                survivors.append(i)
                continue
            while survivors:
                foe = survivors.pop()
                foe_hp = healths[foe]
                atk_hp = healths[i]
                if foe_hp > atk_hp:
                    healths[foe] = foe_hp - 1
                    survivors.append(foe)
                    healths[i] = 0
                    break
                if foe_hp < atk_hp:
                    healths[foe] = 0
                    healths[i] = atk_hp - 1
                else:
                    healths[foe] = 0
                    healths[i] = 0
                    break
        return [hp for hp in healths if hp > 0]

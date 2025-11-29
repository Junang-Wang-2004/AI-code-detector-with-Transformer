class Solution(object):
    def minDamage(self, power, damage, health):
        monsters = sorted(((health[i] + power - 1) // power / damage[i],
                           (health[i] + power - 1) // power,
                           damage[i])
                          for i in range(len(health)))
        total_damage = 0
        cumulative_turns = 0
        for _, turns, dmg in monsters:
            cumulative_turns += turns
            total_damage += cumulative_turns * dmg
        return total_damage

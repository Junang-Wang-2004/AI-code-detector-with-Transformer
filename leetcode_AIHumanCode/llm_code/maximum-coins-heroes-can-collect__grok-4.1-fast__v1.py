class Solution:
    def maximumCoins(self, heroes, monsters, coins):
        import bisect
        enemy_pairs = sorted(zip(monsters, coins))
        total = [0] * (len(enemy_pairs) + 1)
        for pos in range(len(enemy_pairs)):
            total[pos + 1] = total[pos] + enemy_pairs[pos][1]
        ans = [0] * len(heroes)
        for i, strength in enumerate(heroes):
            split = bisect.bisect_right(enemy_pairs, (strength, float('inf')))
            ans[i] = total[split]
        return ans

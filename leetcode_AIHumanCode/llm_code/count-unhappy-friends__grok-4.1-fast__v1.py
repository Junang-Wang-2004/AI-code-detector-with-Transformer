class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        pref_rank = [[0] * n for _ in range(n)]
        for person in range(n):
            for position, target in enumerate(preferences[person]):
                pref_rank[person][target] = position
        partner_of = [-1] * n
        for a, b in pairs:
            partner_of[a] = b
            partner_of[b] = a
        unhappy_count = 0
        for x in range(n):
            current_partner = partner_of[x]
            is_unhappy = False
            for y in range(n):
                if y == x or y == current_partner:
                    continue
                x_pref_y_over_partner = pref_rank[x][y] < pref_rank[x][current_partner]
                y_pref_x_over_partner = pref_rank[y][x] < pref_rank[y][partner_of[y]]
                if x_pref_y_over_partner and y_pref_x_over_partner:
                    is_unhappy = True
                    break
            if is_unhappy:
                unhappy_count += 1
        return unhappy_count

class Solution:
    def connectTwoGroups(self, cost):
        m = len(cost)
        n = len(cost[0]) if m else 0
        full_mask = 1 << n
        INF = float("inf")
        prev_state = [INF] * full_mask
        prev_state[0] = 0
        for group in cost:
            next_state = [INF] * full_mask
            for covered in range(full_mask):
                if prev_state[covered] == INF: continue
                for connect in range(n):
                    updated_mask = covered | (1 << connect)
                    next_state[updated_mask] = min(next_state[updated_mask], prev_state[covered] + group[connect])
            for connect in range(n):
                bitmask = 1 << connect
                for covered in range(full_mask):
                    if next_state[covered] == INF: continue
                    updated_mask = covered | bitmask
                    next_state[updated_mask] = min(next_state[updated_mask], next_state[covered] + group[connect])
            prev_state = next_state
        return prev_state[full_mask - 1]

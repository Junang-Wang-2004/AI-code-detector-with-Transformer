from collections import defaultdict

class Solution:
    def minTransfers(self, transactions):
        balance = defaultdict(int)
        for sender, receiver, amount in transactions:
            balance[sender] += amount
            balance[receiver] -= amount
        residuals = [amt for amt in balance.values() if amt != 0]
        num = len(residuals)
        if num == 0:
            return 0
        total_states = 1 << num
        group_sums = [0] * total_states
        for state in range(total_states):
            for idx in range(num):
                if state & (1 << idx):
                    group_sums[state] += residuals[idx]
        max_parts = [0] * total_states
        for state in range(1, total_states):
            best_prior = 0
            for idx in range(num):
                if state & (1 << idx):
                    prior_state = state ^ (1 << idx)
                    best_prior = max(best_prior, max_parts[prior_state])
            bonus = 1 if group_sums[state] == 0 else 0
            max_parts[state] = best_prior + bonus
        return num - max_parts[-1]

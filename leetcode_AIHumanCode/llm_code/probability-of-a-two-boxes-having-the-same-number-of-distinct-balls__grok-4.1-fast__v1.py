class Solution:
    def getProbability(self, balls):
        def choose(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
            return res

        states = {(0, 0): 1}
        N = sum(balls)
        for num_balls in balls:
            next_states = {}
            for (balance, col_balance), cnt_ways in states.items():
                for pick in range(num_balls + 1):
                    ways = choose(num_balls, pick)
                    new_balance = balance + 2 * pick - num_balls
                    new_col = col_balance - 1 if pick == 0 else col_balance + 1 if pick == num_balls else col_balance
                    next_states[(new_balance, new_col)] = next_states.get((new_balance, new_col), 0) + cnt_ways * ways
            states = next_states
        fav = states.get((0, 0), 0)
        total = choose(N, N // 2)
        return fav / total

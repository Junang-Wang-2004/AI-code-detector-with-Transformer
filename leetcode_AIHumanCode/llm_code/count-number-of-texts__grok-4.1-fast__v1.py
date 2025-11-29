class Solution:
    def countTexts(self, pressedKeys):
        MOD = 10**9 + 7
        result = 1
        n = len(pressedKeys)
        idx = 0
        while idx < n:
            start = idx
            curr_key = pressedKeys[idx]
            while idx < n and pressedKeys[idx] == curr_key:
                idx += 1
            streak_len = idx - start
            max_press = 4 if curr_key in '79' else 3
            ways = [0] * (streak_len + 1)
            ways[0] = 1
            for pos in range(1, streak_len + 1):
                for press in range(1, min(max_press, pos) + 1):
                    ways[pos] = (ways[pos] + ways[pos - press]) % MOD
            result = (result * ways[streak_len]) % MOD
        return result

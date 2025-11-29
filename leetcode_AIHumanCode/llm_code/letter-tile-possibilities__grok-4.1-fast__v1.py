class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0] * 26
        for c in tiles:
            freq[ord(c) - 65] += 1
        
        def explore(state):
            res = 0
            for idx in range(26):
                if state[idx] > 0:
                    state[idx] -= 1
                    res += 1 + explore(state)
                    state[idx] += 1
            return res
        
        return explore(freq)

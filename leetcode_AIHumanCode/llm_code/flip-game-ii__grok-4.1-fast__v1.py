class Solution:
    def canWin(self, s: str) -> bool:
        n = len(s)
        groups = []
        pos = 0
        while pos < n:
            if s[pos] == '+':
                begin = pos
                while pos < n and s[pos] == '+':
                    pos += 1
                groups.append(pos - begin)
            else:
                pos += 1
        if not groups:
            return False
        max_group = max(groups)
        nimbers = [0] * (max_group + 1)
        for length in range(2, max_group + 1):
            moves = set()
            for prefix in range(length - 1):
                suffix = length - prefix - 2
                moves.add(nimbers[prefix] ^ nimbers[suffix])
            mex_val = 0
            while mex_val in moves:
                mex_val += 1
            nimbers[length] = mex_val
        total = 0
        for group in groups:
            total ^= nimbers[group]
        return total != 0

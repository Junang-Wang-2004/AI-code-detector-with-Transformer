class Solution(object):
    def substringXorQueries(self, s, queries):
        if not queries:
            return []
        max_val = max(a ^ b for a, b in queries)
        positions = {}
        first_zero = -1
        for k, ch in enumerate(s):
            if ch == '0' and first_zero == -1:
                first_zero = k
        if first_zero != -1:
            positions[0] = [first_zero, first_zero]
        for start_idx in range(len(s)):
            if s[start_idx] != '1':
                continue
            accum = 0
            for end_idx in range(start_idx, len(s)):
                accum = (accum << 1) | int(s[end_idx])
                if accum > max_val:
                    break
                if accum not in positions:
                    positions[accum] = [start_idx, end_idx]
        output = []
        for x, y in queries:
            val = x ^ y
            output.append(positions.get(val, [-1, -1]))
        return output

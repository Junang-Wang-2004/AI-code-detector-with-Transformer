class Solution(object):
    def minCostGoodCaption(self, caption):
        group_len = 3
        length = len(caption)
        if length < group_len:
            return ""
        ascii_vals = [ord(ch) - ord('a') for ch in caption]
        starts_count = length - group_len + 1
        costs = [[0] * 26 for _ in range(starts_count)]
        lengths = [[0] * 26 for _ in range(starts_count)]
        best_opts = [[0, 0] for _ in range(starts_count)]
        for start in range(starts_count - 1, -1, -1):
            if start == starts_count - 1:
                for let in range(26):
                    seg_cost = sum(abs(ascii_vals[k] - let) for k in range(start, start + group_len))
                    costs[start][let] = seg_cost
                    lengths[start][let] = group_len
                best_opts[start] = min((costs[start][let], let) for let in range(26))
                continue
            for let in range(26):
                single_cost = abs(ascii_vals[start] - let) + costs[start + 1][let]
                costs[start][let] = single_cost
                lengths[start][let] = 1
                if start + group_len < length - 2:
                    next_cost, next_let = best_opts[start + group_len]
                    triple_cost = next_cost + sum(abs(ascii_vals[k] - let) for k in range(start, start + group_len))
                    if triple_cost < costs[start][let] or (triple_cost == costs[start][let] and next_let < let):
                        costs[start][let] = triple_cost
                        lengths[start][let] = group_len
            best_opts[start] = min((costs[start][let], let) for let in range(26))
        parts = []
        curr_pos = 0
        curr_let = best_opts[0][1]
        curr_length = 1
        while curr_pos != length:
            if curr_length == group_len:
                curr_let = best_opts[curr_pos][1]
            curr_length = lengths[curr_pos][curr_let]
            parts.append(chr(ord('a') + curr_let) * curr_length)
            curr_pos += curr_length
        return "".join(parts)

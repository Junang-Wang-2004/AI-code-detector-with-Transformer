class Solution(object):
    def maxRectangleArea(self, xCoord, yCoord):
        x_to_ys = {}
        for i in range(len(xCoord)):
            x = xCoord[i]
            if x not in x_to_ys:
                x_to_ys[x] = []
            x_to_ys[x].append(yCoord[i])
        sorted_xs = sorted(x_to_ys)
        unique_ys = sorted(set(yCoord))
        y_rank = {val: idx + 1 for idx, val in enumerate(unique_ys)}
        comp_size = len(unique_ys)

        class FenwickTree(object):
            def __init__(self, size):
                self.size = size
                self.data = [0] * (size + 2)

            def modify(self, pos, amount):
                while pos <= self.size:
                    self.data[pos] += amount
                    pos += pos & -pos

            def sum_up_to(self, pos):
                total = 0
                while pos > 0:
                    total += self.data[pos]
                    pos -= pos & -pos
                return total

        ft = FenwickTree(comp_size)
        memo = {}
        max_area = -1
        for curr_x in sorted_xs:
            curr_ys = sorted(x_to_ys[curr_x])
            if len(curr_ys) >= 2:
                for pos in range(len(curr_ys) - 1):
                    bot_y = curr_ys[pos]
                    top_y = curr_ys[pos + 1]
                    bot_id = y_rank[bot_y]
                    top_id = y_rank[top_y]
                    prior_in_range = ft.sum_up_to(top_id) - ft.sum_up_to(bot_id - 1)
                    pair = (bot_id, top_id)
                    if pair in memo and memo[pair][0] == prior_in_range:
                        width = curr_x - memo[pair][1]
                        height = top_y - bot_y
                        area = width * height
                        if area > max_area:
                            max_area = area
                    memo[pair] = (prior_in_range + 2, curr_x)
            for y_val in curr_ys:
                ft.modify(y_rank[y_val], 1)
        return max_area

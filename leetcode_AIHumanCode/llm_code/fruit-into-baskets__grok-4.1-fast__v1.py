class Solution(object):
    def totalFruit(self, tree):
        last_pos = {}
        left = 0
        max_len = 0
        for curr in range(len(tree)):
            last_pos[tree[curr]] = curr
            if len(last_pos) > 2:
                to_remove = min(last_pos, key=last_pos.get)
                start_pos = last_pos[to_remove]
                del last_pos[to_remove]
                left = start_pos + 1
            max_len = max(max_len, curr - left + 1)
        return max_len

class Solution(object):
    def minimumLevel(self, root):
        level_info = []
        curr_lev = [root]
        lev_idx = 1
        while curr_lev:
            nxt_lev = []
            lev_total = 0
            for nd in curr_lev:
                lev_total += nd.val
                if nd.left:
                    nxt_lev.append(nd.left)
                if nd.right:
                    nxt_lev.append(nd.right)
            level_info.append((lev_total, lev_idx))
            curr_lev = nxt_lev
            lev_idx += 1
        return min(level_info)[-1]

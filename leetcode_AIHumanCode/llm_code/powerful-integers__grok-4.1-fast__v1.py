class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        ans = set()
        xs = []
        cur_x = 1
        while cur_x <= bound:
            xs.append(cur_x)
            if x == 1:
                break
            cur_x *= x
        ys = []
        cur_y = 1
        while cur_y <= bound:
            ys.append(cur_y)
            if y == 1:
                break
            cur_y *= y
        for px in xs:
            for py in ys:
                if px + py <= bound:
                    ans.add(px + py)
        return list(ans)

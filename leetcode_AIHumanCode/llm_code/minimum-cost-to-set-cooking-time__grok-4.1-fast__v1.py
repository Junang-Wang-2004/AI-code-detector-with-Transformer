class Solution:
    def minCostSetTime(self, init_digit, change_cost, press_cost, total_secs):
        def calc_cost(start_d, mv_cost, ps_cost, mins, secs):
            if mins < 0 or mins > 99 or secs > 99:
                return float('inf')
            num = mins * 100 + secs
            digs = []
            if num == 0:
                digs = [0]
            else:
                tmp = num
                while tmp:
                    digs.append(tmp % 10)
                    tmp //= 10
                digs.reverse()
            res = 0
            cur_d = start_d
            for d in digs:
                if d != cur_d:
                    res += mv_cost
                res += ps_cost
                cur_d = d
            return res
        
        minutes, seconds = divmod(total_secs, 60)
        c1 = calc_cost(init_digit, change_cost, press_cost, minutes, seconds)
        c2 = calc_cost(init_digit, change_cost, press_cost, minutes - 1, seconds + 60)
        return min(c1, c2)

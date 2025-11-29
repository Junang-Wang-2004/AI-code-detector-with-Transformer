class Solution:
    def garbageCollection(self, garbage, travel):
        n = len(garbage)
        times = [0] * n
        for i in range(1, n):
            times[i] = times[i - 1] + travel[i - 1]
        pos_g = pos_m = pos_p = -1
        tot_garb = 0
        for i, s in enumerate(garbage):
            tot_garb += len(s)
            for ch in s:
                if ch == 'G':
                    pos_g = i
                elif ch == 'M':
                    pos_m = i
                elif ch == 'P':
                    pos_p = i
        add_time = 0
        if pos_g >= 0:
            add_time += times[pos_g]
        if pos_m >= 0:
            add_time += times[pos_m]
        if pos_p >= 0:
            add_time += times[pos_p]
        return tot_garb + add_time

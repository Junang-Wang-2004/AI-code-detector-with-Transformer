class Solution(object):
    def punishmentNumber(self, n):
        def valid_split(num_str, goal):
            m = len(num_str)
            def explore(idx, rem):
                if idx == m:
                    return rem == 0
                for j in range(idx + 1, m + 1):
                    part = num_str[idx:j]
                    if len(part) > 1 and part[0] == '0':
                        continue
                    val = int(part)
                    if val > rem:
                        break
                    if explore(j, rem - val):
                        return True
                return False
            return explore(0, goal)

        ans = 0
        for k in range(1, n + 1):
            sq_str = str(k * k)
            if valid_split(sq_str, k):
                ans += k * k
        return ans

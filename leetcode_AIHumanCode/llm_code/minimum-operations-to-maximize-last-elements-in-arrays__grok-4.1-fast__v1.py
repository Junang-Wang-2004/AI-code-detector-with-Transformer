class Solution:
    def minOperations(self, a, b):
        n = len(a)
        costs = []
        for flip in range(2):
            tg1 = b[n-1] if flip else a[n-1]
            tg2 = a[n-1] if flip else b[n-1]
            cnt = 0
            feasible = True
            for i in range(n):
                x = a[i]
                y = b[i]
                if x <= tg1 and y <= tg2:
                    continue
                if y <= tg1 and x <= tg2:
                    cnt += 1
                else:
                    feasible = False
                    break
            if feasible:
                costs.append(cnt)
        return min(costs) if costs else -1

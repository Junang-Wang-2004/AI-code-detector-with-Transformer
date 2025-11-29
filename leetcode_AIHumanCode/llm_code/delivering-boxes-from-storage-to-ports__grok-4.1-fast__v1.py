class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        n = len(boxes)
        pre_w = [0] * (n + 1)
        pre_c = [0] * (n + 2)
        for i in range(n):
            pre_w[i + 1] = pre_w[i] + boxes[i][1]
            if i > 0 and boxes[i][0] != boxes[i - 1][0]:
                pre_c[i + 1] = pre_c[i] + 1
            else:
                pre_c[i + 1] = pre_c[i]
        pre_c[n + 1] = pre_c[n]
        dp = [0] * (n + 1)
        from collections import deque
        dq = deque()
        dq.append(0)
        w_left = 0
        for i in range(1, n + 1):
            while w_left < i and pre_w[i] - pre_w[w_left] > maxWeight:
                w_left += 1
            low = max(w_left, i - maxBoxes, 0)
            while dq and dq[0] < low:
                dq.popleft()
            if dq:
                best_j = dq[0]
                best_f = dp[best_j] - pre_c[best_j + 1]
                dp[i] = 2 + pre_c[i] + best_f
            new_f = dp[i] - pre_c[i + 1]
            while dq and (dp[dq[-1]] - pre_c[dq[-1] + 1]) >= new_f:
                dq.pop()
            dq.append(i)
        return dp[n]

class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        pref_count = [0] * (n + 1)
        pref_pos = [0] * (n + 1)
        for i in range(n):
            ball = 1 if boxes[i] == '1' else 0
            pref_count[i + 1] = pref_count[i] + ball
            pref_pos[i + 1] = pref_pos[i] + i * ball
        tot_balls = pref_count[n]
        tot_pos_sum = pref_pos[n]
        res = [0] * n
        for j in range(n):
            lballs = pref_count[j]
            lsum = pref_pos[j]
            rballs = tot_balls - lballs
            rsum = tot_pos_sum - lsum
            res[j] = j * lballs - lsum + rsum - j * rballs
        return res

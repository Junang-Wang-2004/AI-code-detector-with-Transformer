class Solution:
    def minSessions(self, tasks, sessionTime):
        n = len(tasks)
        N = 1 << n
        INF = float('inf')
        num_sessions = [INF] * N
        last_rem = [INF] * N
        num_sessions[0] = 0
        last_rem[0] = sessionTime + 1
        for current in range(N):
            if num_sessions[current] == INF:
                continue
            pos = 1
            for cost in tasks:
                if current & pos:
                    pos <<= 1
                    continue
                next_state = current | pos
                prev_rem = last_rem[current]
                if prev_rem + cost <= sessionTime:
                    cand_sess = num_sessions[current]
                    cand_rem = prev_rem + cost
                else:
                    cand_sess = num_sessions[current] + 1
                    cand_rem = cost
                if (cand_sess < num_sessions[next_state] or
                    (cand_sess == num_sessions[next_state] and cand_rem < last_rem[next_state])):
                    num_sessions[next_state] = cand_sess
                    last_rem[next_state] = cand_rem
                pos <<= 1
        return num_sessions[N - 1]

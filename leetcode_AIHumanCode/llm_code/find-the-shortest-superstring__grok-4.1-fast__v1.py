class Solution:
    def shortestSuperstring(self, A):
        n = len(A)
        ovlp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ln_i, ln_j = len(A[i]), len(A[j])
                for k in range(min(ln_i, ln_j), -1, -1):
                    if A[i][-k:] == A[j][:k]:
                        ovlp[i][j] = k
                        break
        INF = 10**9
        dist = [[INF] * n for _ in range(1 << n)]
        track = [[-1] * n for _ in range(1 << n)]
        for i in range(n):
            m = 1 << i
            dist[m][i] = len(A[i])
        for m in range(1 << n):
            for u in range(n):
                if (m & (1 << u)) == 0 or dist[m][u] == INF:
                    continue
                for v in range(n):
                    if m & (1 << v):
                        continue
                    nm = m | (1 << v)
                    added = len(A[v]) - ovlp[u][v]
                    nc = dist[m][u] + added
                    if nc < dist[nm][v]:
                        dist[nm][v] = nc
                        track[nm][v] = u
        fm = (1 << n) - 1
        minl = INF
        fin = -1
        for j in range(n):
            if dist[fm][j] < minl:
                minl = dist[fm][j]
                fin = j
        seq = []
        cm = fm
        ce = fin
        while ce != -1:
            seq.append(ce)
            pu = track[cm][ce]
            cm ^= (1 << ce)
            ce = pu
        seq.reverse()
        if not seq:
            return ""
        ans = A[seq[0]]
        for idx in range(1, len(seq)):
            pidx = seq[idx - 1]
            o = ovlp[pidx][seq[idx]]
            ans += A[seq[idx]][o:]
        return ans

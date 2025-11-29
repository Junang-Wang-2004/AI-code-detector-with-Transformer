class Solution:
    def maximumBobPoints(self, numArrows, aliceArrows):
        n = len(aliceArrows)
        top_score = [-1]
        top_dist = [None]
        shots = [0] * n
        
        def explore(idx, avail):
            if idx == -1:
                shots[n - 1] += avail
                this_score = sum(k for k, a in enumerate(aliceArrows) if shots[k] > a)
                if this_score > top_score[0]:
                    top_score[0] = this_score
                    top_dist[0] = shots[:]
                shots[n - 1] -= avail
                return
            shots[idx] = 0
            explore(idx - 1, avail)
            req = aliceArrows[idx] + 1
            if avail >= req:
                shots[idx] = req
                explore(idx - 1, avail - req)
                shots[idx] = 0
        
        explore(n - 1, numArrows)
        return top_dist[0]

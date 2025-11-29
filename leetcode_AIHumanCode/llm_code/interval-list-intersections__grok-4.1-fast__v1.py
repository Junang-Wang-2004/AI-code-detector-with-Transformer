class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def intervalIntersection(self, A, B):
        matches = []
        pa = pb = 0
        while pa < len(A) and pb < len(B):
            o_start = max(A[pa].start, B[pb].start)
            o_end = min(A[pa].end, B[pb].end)
            if o_start <= o_end:
                matches.append(Interval(o_start, o_end))
            if A[pa].end <= B[pb].end:
                pa += 1
            else:
                pb += 1
        return matches

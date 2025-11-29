import bisect

class C1:

    def __init__(self):
        self.recording_times = []
        self.cumulative_scores = [0]
        self.running_total = 0

    def record(self, a1, a2):
        self.recording_times.append(a1)
        self.running_total += a2
        self.cumulative_scores.append(self.running_total)

    def totalScore(self, a1, a2):
        v1 = bisect.bisect_left(self.recording_times, a1)
        v2 = bisect.bisect_right(self.recording_times, a2) - 1
        return self.cumulative_scores[v2 + 1] - self.cumulative_scores[v1]

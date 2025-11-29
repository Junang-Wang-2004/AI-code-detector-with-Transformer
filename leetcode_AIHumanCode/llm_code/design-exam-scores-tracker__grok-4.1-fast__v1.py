import bisect

class ExamTracker:
    def __init__(self):
        self.recording_times = []
        self.cumulative_scores = [0]
        self.running_total = 0

    def record(self, time_stamp, score_value):
        self.recording_times.append(time_stamp)
        self.running_total += score_value
        self.cumulative_scores.append(self.running_total)

    def totalScore(self, start_time, end_time):
        left_index = bisect.bisect_left(self.recording_times, start_time)
        right_index = bisect.bisect_right(self.recording_times, end_time) - 1
        return self.cumulative_scores[right_index + 1] - self.cumulative_scores[left_index]

class Solution:
    def numberOfRounds(self, startTime, finishTime):
        def to_minutes(time_str):
            return int(time_str[0:2]) * 60 + int(time_str[3:5])
        begin = to_minutes(startTime)
        end = to_minutes(finishTime)
        if begin > end:
            end += 1440
        start_round = begin // 15 + (1 if begin % 15 else 0)
        end_round = end // 15
        return max(end_round - start_round, 0)

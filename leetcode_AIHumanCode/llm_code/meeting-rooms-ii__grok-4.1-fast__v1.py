class Solution:
    def minMeetingRooms(self, intervals):
        events = []
        for begin, finish in intervals:
            events.append((begin, 1))
            events.append((finish, -1))
        events.sort()
        peak, active = 0, 0
        for _, adjustment in events:
            active += adjustment
            if active > peak:
                peak = active
        return peak

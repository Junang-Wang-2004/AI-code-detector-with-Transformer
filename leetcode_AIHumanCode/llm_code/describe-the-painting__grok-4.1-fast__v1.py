class Solution:
    def splitPainting(self, segments):
        events = []
        for start, end, color in segments:
            events.append((start, color))
            events.append((end, -color))
        events.sort(key=lambda x: x[0])
        
        result = []
        active_color = 0
        last_pos = None
        idx = 0
        while idx < len(events):
            pos = events[idx][0]
            if last_pos is not None and active_color > 0:
                result.append([last_pos, pos, active_color])
            while idx < len(events) and events[idx][0] == pos:
                active_color += events[idx][1]
                idx += 1
            last_pos = pos
        return result

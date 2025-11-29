from collections import deque

class Solution(object):
    def movesToStamp(self, stamp, target):
        stamp_len = len(stamp)
        target_len = len(target)
        if stamp_len == 0:
            return []
        starts_count = target_len - stamp_len + 1
        rem_mismatches = [0] * starts_count
        match_positions = [[] for _ in range(starts_count)]
        waiting_stamps = [[] for _ in range(target_len)]
        for start in range(starts_count):
            for offset in range(stamp_len):
                pos = start + offset
                if target[pos] == stamp[offset]:
                    match_positions[start].append(pos)
                else:
                    rem_mismatches[start] += 1
                    waiting_stamps[pos].append(start)
        pos_queue = deque()
        position_done = [False] * target_len
        sequence = []
        for start in range(starts_count):
            if rem_mismatches[start] == 0:
                sequence.append(start)
                for pos in match_positions[start]:
                    if not position_done[pos]:
                        position_done[pos] = True
                        pos_queue.append(pos)
        while pos_queue:
            curr_pos = pos_queue.popleft()
            for start in waiting_stamps[curr_pos]:
                rem_mismatches[start] -= 1
                if rem_mismatches[start] == 0:
                    sequence.append(start)
                    for pos in match_positions[start]:
                        if not position_done[pos]:
                            position_done[pos] = True
                            pos_queue.append(pos)
        return sequence[::-1] if all(position_done) else []

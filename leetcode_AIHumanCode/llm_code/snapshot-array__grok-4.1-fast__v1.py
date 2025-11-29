import collections

class SnapshotArray:

    def __init__(self, length):
        self.records = collections.defaultdict(list)
        self.snap_cnt = 0

    def set(self, index, val):
        rec = self.records[index]
        if rec and rec[-1][0] == self.snap_cnt:
            rec[-1][1] = val
        else:
            rec.append([self.snap_cnt, val])

    def snap(self):
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, index, snap_id):
        rec = self.records[index]
        left, right = 0, len(rec) - 1
        while left <= right:
            mid = (left + right) // 2
            if rec[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            return rec[right][1]
        return 0

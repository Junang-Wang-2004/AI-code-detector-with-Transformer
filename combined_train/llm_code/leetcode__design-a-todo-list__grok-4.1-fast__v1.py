import bisect
import collections

class C1:

    def __init__(self):
        self.all_tasks = []
        self.by_user = collections.defaultdict(list)
        self.by_user_tag = collections.defaultdict(lambda: collections.defaultdict(list))

    def addTask(self, a1, a2, a3, a4):
        v1 = set(a4)
        self.all_tasks.append((a3, a2, v1))
        v2 = len(self.all_tasks)
        v3 = (a3, v2)
        bisect.insort(self.by_user[a1], v3)
        for v4 in v1:
            bisect.insort(self.by_user_tag[a1][v4], v3)
        return v2

    def getAllTasks(self, a1):
        if a1 not in self.by_user:
            return []
        v1 = self.by_user[a1]
        return [self.all_tasks[idx - 1][1] for v2, v3 in v1]

    def getTasksForTag(self, a1, a2):
        if a1 not in self.by_user_tag:
            return []
        v1 = self.by_user_tag[a1]
        if a2 not in v1:
            return []
        v2 = v1[a2]
        return [self.all_tasks[idx - 1][1] for v3, v4 in v2]

    def completeTask(self, a1, a2):
        if not (1 <= a2 <= len(self.all_tasks) and a1 in self.by_user):
            return
        v1, v2, v3 = self.all_tasks[a2 - 1]
        v4 = (v1, a2)
        v5 = self.by_user[a1]
        v6 = bisect.bisect_left(v5, v4)
        if v6 < len(v5) and v5[v6] == v4:
            del v5[v6]
        for v7 in v3:
            v8 = self.by_user_tag[a1][v7]
            v6 = bisect.bisect_left(v8, v4)
            if v6 < len(v8) and v8[v6] == v4:
                del v8[v6]

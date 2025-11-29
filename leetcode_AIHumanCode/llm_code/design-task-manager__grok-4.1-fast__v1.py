import heapq

class TaskManager:
    def __init__(self, tasks):
        self.active_tasks = {}
        self.min_heap = []
        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, user_id, task_id, priority):
        heapq.heappush(self.min_heap, (-priority, -task_id, -user_id))
        self.active_tasks[task_id] = (user_id, priority)

    def edit(self, task_id, new_priority):
        if task_id in self.active_tasks:
            user_id = self.active_tasks[task_id][0]
            self.rmv(task_id)
            self.add(user_id, task_id, new_priority)

    def rmv(self, task_id):
        self.active_tasks.pop(task_id, None)

    def execTop(self):
        while self.min_heap:
            np, nt, nu = self.min_heap[0]
            tid = -nt
            prio = -np
            if tid in self.active_tasks and self.active_tasks[tid][1] == prio:
                heapq.heappop(self.min_heap)
                uid = -nu
                self.rmv(tid)
                return uid
            heapq.heappop(self.min_heap)
        return -1

import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        occupied = []
        res = []
        cur_time = 0
        for tsk_time in range(len(tasks)):
            cur_time = max(cur_time, tsk_time)
            while occupied and occupied[0][0] <= cur_time:
                done_time, wt, srv_id = heapq.heappop(occupied)
                heapq.heappush(available, (wt, srv_id))
            if not available:
                cur_time = occupied[0][0]
                while occupied and occupied[0][0] <= cur_time:
                    done_time, wt, srv_id = heapq.heappop(occupied)
                    heapq.heappush(available, (wt, srv_id))
            wt, srv_id = heapq.heappop(available)
            end_time = cur_time + tasks[tsk_time]
            heapq.heappush(occupied, (end_time, wt, srv_id))
            res.append(srv_id)
        return res

class Solution:
    def countServers(self, n, logs, x, queries):
        events = []
        for srv_id, tm in logs:
            srv_idx = srv_id - 1
            events.append((tm, 0, 1, srv_idx))
            events.append((tm + x + 1, 0, -1, srv_idx))
        for qid, qt in enumerate(queries):
            events.append((qt, 1, 0, qid))
        events.sort(key=lambda e: (e[0], e[1]))
        server_load = [0] * n
        busy_servers = 0
        answer = [0] * len(queries)
        for _, typ, change, ident in events:
            if typ == 0:
                srv = ident
                before = server_load[srv]
                server_load[srv] += change
                after = server_load[srv]
                if before == 0 and after > 0:
                    busy_servers += 1
                elif before > 0 and after == 0:
                    busy_servers -= 1
            else:
                answer[ident] = n - busy_servers
        return answer

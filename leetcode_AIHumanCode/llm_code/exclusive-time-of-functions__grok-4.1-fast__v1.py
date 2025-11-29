class Solution:
    def exclusiveTime(self, n, logs):
        runtimes = [0] * n
        active_funcs = []
        prior_time = 0
        for record in logs:
            parts = record.split(':')
            f_id = int(parts[0])
            act_type = parts[1]
            curr_time = int(parts[2])
            time_diff = curr_time - prior_time
            if active_funcs:
                runtimes[active_funcs[-1]] += time_diff
                if act_type == 'end':
                    runtimes[active_funcs[-1]] += 1
                    active_funcs.pop()
            if act_type == 'start':
                active_funcs.append(f_id)
            prior_time = curr_time if act_type == 'start' else curr_time + 1
        return runtimes

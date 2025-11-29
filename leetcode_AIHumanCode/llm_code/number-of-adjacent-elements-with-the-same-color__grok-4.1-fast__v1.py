class Solution:
    def colorTheArray(self, n, queries):
        painting = [0] * n
        active_connections = 0
        outcomes = [0] * len(queries)
        for query_index in range(len(queries)):
            spot, hue = queries[query_index]
            if painting[spot]:
                deductions = 0
                if spot > 0 and painting[spot - 1] == painting[spot]:
                    deductions += 1
                if spot + 1 < n and painting[spot + 1] == painting[spot]:
                    deductions += 1
                active_connections -= deductions
            painting[spot] = hue
            if painting[spot]:
                additions = 0
                if spot > 0 and painting[spot - 1] == painting[spot]:
                    additions += 1
                if spot + 1 < n and painting[spot + 1] == painting[spot]:
                    additions += 1
                active_connections += additions
            outcomes[query_index] = active_connections
        return outcomes

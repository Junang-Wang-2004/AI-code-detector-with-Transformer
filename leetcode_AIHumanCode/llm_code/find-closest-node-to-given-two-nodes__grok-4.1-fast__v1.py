class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)
        dist_from_1 = [-1] * n
        curr = node1
        steps = 0
        while curr != -1 and dist_from_1[curr] == -1:
            dist_from_1[curr] = steps
            steps += 1
            curr = edges[curr]
        
        dist_from_2 = [-1] * n
        curr = node2
        steps = 0
        while curr != -1 and dist_from_2[curr] == -1:
            dist_from_2[curr] = steps
            steps += 1
            curr = edges[curr]
        
        result = -1
        min_max_dist = float('inf')
        for i in range(n):
            if dist_from_1[i] != -1 and dist_from_2[i] != -1:
                this_max = max(dist_from_1[i], dist_from_2[i])
                if this_max < min_max_dist or (this_max == min_max_dist and i < result):
                    min_max_dist = this_max
                    result = i
        return result

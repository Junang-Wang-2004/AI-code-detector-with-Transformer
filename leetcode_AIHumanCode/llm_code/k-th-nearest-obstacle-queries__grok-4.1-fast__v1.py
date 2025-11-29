import heapq

class Solution:
    def resultsArray(self, queries, k):
        pq = []
        output = []
        for point in queries:
            distance = abs(point[0]) + abs(point[1])
            if len(pq) < k:
                heapq.heappush(pq, -distance)
            elif distance < -pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, -distance)
            if len(pq) == k:
                output.append(-pq[0])
            else:
                output.append(-1)
        return output

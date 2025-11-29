import heapq

class Solution:
    def halveArray(self, nums):
        pq = [-val for val in nums]
        heapq.heapify(pq)
        req_reduction = sum(nums) / 2
        achieved = 0.0
        moves = 0
        while achieved < req_reduction:
            top = -heapq.heappop(pq)
            halved = top / 2
            achieved += halved
            if achieved < req_reduction:
                heapq.heappush(pq, -halved)
            moves += 1
        return moves

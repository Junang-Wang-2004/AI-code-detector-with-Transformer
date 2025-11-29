class Solution:
    def canSeePersonsCount(self, heights):
        n = len(heights)
        answer = [0] * n
        monotonic = []
        for position in range(n - 1, -1, -1):
            visible_count = 0
            while monotonic and heights[monotonic[-1]] < heights[position]:
                monotonic.pop()
                visible_count += 1
            if monotonic:
                visible_count += 1
            answer[position] = visible_count
            if monotonic and heights[monotonic[-1]] == heights[position]:
                monotonic.pop()
            monotonic.append(position)
        return answer

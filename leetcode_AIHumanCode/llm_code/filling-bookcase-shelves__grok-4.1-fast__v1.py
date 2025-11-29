class Solution:
    def minHeightShelves(self, books, shelf_width):
        num_books = len(books)
        INF = float('inf')
        min_cost = [INF] * (num_books + 1)
        min_cost[0] = 0
        for end in range(1, num_books + 1):
            curr_width = 0
            curr_height = 0
            pos = end - 1
            while pos >= 0:
                curr_width += books[pos][0]
                curr_height = max(curr_height, books[pos][1])
                if curr_width > shelf_width:
                    break
                min_cost[end] = min(min_cost[end], min_cost[pos] + curr_height)
                pos -= 1
        return min_cost[num_books]

from typing import List
import collections

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        def compute_area(maximum_height: int, segment_size: int) -> int:
            bottom = max(maximum_height - segment_size + 1, 0)
            count_terms = maximum_height - bottom + 1
            return (bottom + maximum_height) * count_terms // 2
        
        length = len(books)
        best = 0
        running_total = 0
        pile = collections.deque([-1])
        
        for end in range(length):
            while pile[-1] != -1 and books[pile[-1]] >= books[end] - (end - pile[-1]):
                removed_end = pile.pop()
                running_total -= compute_area(

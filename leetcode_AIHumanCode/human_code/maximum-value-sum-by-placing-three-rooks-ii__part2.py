# Time:  O(m * n * logk + nCr((k-1)*(2*k-1)+1), k) * k) = O(m * n)
# Space: O(k * (m + n)) = O(m + n)
import heapq
import itertools


# heap, brute force
class Solution2(object):
    def maximumValueSum(self, board):
        """
        """
        k = 3
        rows = [heapq.nlargest(k, [(board[i][j], i, j) for j in range(len(board[0]))]) for i in range(len(board))]
        cols = [heapq.nlargest(k, [(board[i][j], i, j) for i in range(len(board))]) for j in range(len(board[0]))]
        min_heap = heapq.nlargest((k-1)*(2*k-1)+1, set(itertools.chain(*rows)) & set(itertools.chain(*cols)))  # each choice excludes at most 2k-1 candidates, we should have at least (k-1)*(2k-1)+1 candidates
        return max(sum(x[0] for x in c) for c in itertools.combinations(min_heap, k) if len({x[1] for x in c}) == k == len({x[2] for x in c}))

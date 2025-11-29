# Time:  O((b+h) * h!*(b+h-1)!/(b-1)!)
# Space: O((b+h) * h!*(b+h-1)!/(b-1)!)
import collections


# brute force solution
class Solution_TLE(object):
    def findMinStep(self, board, hand):
        """
        """
        def shrink(s):  # Time: O(n), Space: O(n)
            stack = []
            start = 0
            for i in range(len(s)+1):
                if i == len(s) or s[i] != s[start]:
                    if stack and stack[-1][0] == s[start]:
                        stack[-1][1] += i - start
                        if stack[-1][1] >= 3:
                            stack.pop()
                    elif s and i - start < 3:
                        stack += [s[start], i - start],
                    start = i
            result = []
            for p in stack:
                result += [p[0]] * p[1]
            return result

        def findMinStepHelper(board, hand, lookup):
            if not board: return 0
            if not hand: return float("inf")
            if tuple(hand) in lookup[tuple(board)]: return lookup[tuple(board)][tuple(hand)]

            result = float("inf")
            for i in range(len(hand)):
                for j in range(len(board)+1):
                    next_board = shrink(board[0:j] + hand[i:i+1] + board[j:])
                    next_hand = hand[0:i] + hand[i+1:]
                    result = min(result, findMinStepHelper(next_board, next_hand, lookup) + 1)
            lookup[tuple(board)][tuple(hand)] = result
            return result

        lookup = collections.defaultdict(dict)
        board, hand = list(board), list(hand)
        result = findMinStepHelper(board, hand, lookup)
        return -1 if result == float("inf") else result



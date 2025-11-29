class Solution(object):
    def shortestSequence(self, rolls, k):
        n = len(rolls)
        idx = 0
        answer = 1
        while idx < n:
            current = set()
            uniques = 0
            while idx < n and uniques < k:
                roll = rolls[idx]
                if roll not in current:
                    current.add(roll)
                    uniques += 1
                idx += 1
            if uniques == k:
                answer += 1
        return answer

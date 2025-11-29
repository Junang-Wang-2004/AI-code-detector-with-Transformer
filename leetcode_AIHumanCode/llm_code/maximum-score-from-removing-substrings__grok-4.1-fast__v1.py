class Solution(object):
    def maximumGain(self, s, x, y):
        def eliminate(st, first, second, points):
            score = 0
            stack = []
            for char in st:
                stack.append(char)
                while len(stack) >= 2 and stack[-2] == first and stack[-1] == second:
                    stack.pop()
                    stack.pop()
                    score += points
            return score, ''.join(stack)

        if x >= y:
            part1, leftover = eliminate(s, 'a', 'b', x)
            part2, _ = eliminate(leftover, 'b', 'a', y)
            return part1 + part2
        else:
            part1, leftover = eliminate(s, 'b', 'a', y)
            part2, _ = eliminate(leftover, 'a', 'b', x)
            return part1 + part2

class Solution:
    def calPoints(self, ops):
        scores = []
        total = 0
        for operation in ops:
            if operation == '+':
                val = scores[-1] + scores[-2]
                scores.append(val)
                total += val
            elif operation == 'D':
                val = scores[-1] * 2
                scores.append(val)
                total += val
            elif operation == 'C':
                last_score = scores.pop()
                total -= last_score
            else:
                val = int(operation)
                scores.append(val)
                total += val
        return total

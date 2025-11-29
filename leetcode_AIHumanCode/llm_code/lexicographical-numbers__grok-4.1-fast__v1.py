class Solution(object):
    def lexicalOrder(self, n):
        output = []
        pile = []
        for start_digit in range(9, 0, -1):
            if start_digit <= n:
                pile.append(start_digit)
        while pile and len(output) < n:
            active = pile.pop()
            output.append(active)
            for extra_digit in range(9, 0, -1):
                successor = active * 10 + extra_digit
                if successor <= n:
                    pile.append(successor)
            zero_successor = active * 10
            if zero_successor <= n:
                pile.append(zero_successor)
        return output

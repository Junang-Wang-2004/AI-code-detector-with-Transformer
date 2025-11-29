class Solution:
    def generateParenthesis(self, n):
        combos = [[] for _ in range(n + 1)]
        combos[0] = [""]
        for size in range(1, n + 1):
            ways = []
            for pos in range(size):
                for front in combos[pos]:
                    for back in combos[size - 1 - pos]:
                        ways.append("(" + front + ")" + back)
            combos[size] = ways
        return combos[n]

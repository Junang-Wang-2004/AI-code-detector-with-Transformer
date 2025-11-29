# Time:  O(n^2)
# Space: O(n)
class Solution2(object):
    def findSecretWord(self, wordlist, master):
        """
        """
        def solve(H, possible):
            min_max_group, best_guess = possible, None
            for guess in possible:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[H[guess][j]].append(j)
                max_group = max(groups, key=len)
                if len(max_group) < len(min_max_group):
                    min_max_group, best_guess = max_group, guess
            return best_guess

        H = [[sum(a == b for a, b in zip(wordlist[i], wordlist[j]))
                  for j in range(len(wordlist))]
                  for i in range(len(wordlist))]
        possible = list(range(len(wordlist)))
        n = 0
        while n < 6:
            guess = solve(H, possible)
            n = master.guess(wordlist[guess])
            possible = [j for j in possible if H[guess][j] == n]



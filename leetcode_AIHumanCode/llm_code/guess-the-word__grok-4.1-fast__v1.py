class Solution:
    def findSecretWord(self, wordlist, master):
        N = len(wordlist)
        sim_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                matches = sum(wordlist[i][k] == wordlist[j][k] for k in range(6))
                sim_matrix[i][j] = sim_matrix[j][i] = matches
        for i in range(N):
            sim_matrix[i][i] = 6

        remain = set(range(N))
        for _ in range(6):
            if len(remain) <= 1:
                return
            best_guess = None
            best_max_size = float('inf')
            for g in remain:
                groups = [[] for _ in range(7)]
                for j in remain:
                    if j != g:
                        groups[sim_matrix[g][j]].append(j)
                this_max = max(len(group) for group in groups)
                if this_max < best_max_size:
                    best_max_size = this_max
                    best_guess = g
            actual_matches = master.guess(wordlist[best_guess])
            if actual_matches == 6:
                return
            remain = {j for j in remain if sim_matrix[best_guess][j] == actual_matches}

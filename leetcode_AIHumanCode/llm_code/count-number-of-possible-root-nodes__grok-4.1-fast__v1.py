import collections

class Solution:
    def rootCount(self, edges, guesses, k):
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        pred_set = {(a, b) for a, b in guesses}

        def calc_down(p, node):
            score = 1 if (p, node) in pred_set else 0
            for neigh in graph[node]:
                if neigh != p:
                    score += calc_down(node, neigh)
            return score

        start_score = calc_down(-1, 0)
        count = 0

        def reorient(p, node, score):
            nonlocal count
            score -= 1 if (p, node) in pred_set else 0
            score += 1 if (node, p) in pred_set else 0
            if score >= k:
                count += 1
            for neigh in graph[node]:
                if neigh != p:
                    reorient(node, neigh, score)

        reorient(-1, 0, start_score)
        return count

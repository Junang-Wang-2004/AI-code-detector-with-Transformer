class Solution:
    def areSentencesSimilarTwo(self, sentence1, sentence2, similar_pairs):
        if len(sentence1) != len(sentence2):
            return False
        
        parent = {}
        rank = {}
        
        def get_root(p, node):
            if p[node] != node:
                p[node] = get_root(p, p[node])
            return p[node]
        
        def connect(p, r, a, b):
            root_a = get_root(p, a)
            root_b = get_root(p, b)
            if root_a == root_b:
                return
            if r[root_a] > r[root_b]:
                p[root_b] = root_a
            elif r[root_a] < r[root_b]:
                p[root_a] = root_b
            else:
                p[root_b] = root_a
                r[root_a] += 1
        
        for a, b in similar_pairs:
            if a not in parent:
                parent[a] = a
                rank[a] = 0
            if b not in parent:
                parent[b] = b
                rank[b] = 0
            connect(parent, rank, a, b)
        
        for first, second in zip(sentence1, sentence2):
            if first == second:
                continue
            if first not in parent or second not in parent:
                return False
            if get_root(parent, first) != get_root(parent, second):
                return False
        
        return True

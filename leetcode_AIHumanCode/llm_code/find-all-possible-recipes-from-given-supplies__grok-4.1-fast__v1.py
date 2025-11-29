import collections

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = collections.defaultdict(list)
        deg = {}
        rset = set(recipes)
        for i, r in enumerate(recipes):
            deg[r] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(r)
        res = []
        q = collections.deque(supplies)
        while q:
            u = q.popleft()
            if u in rset:
                res.append(u)
            for v in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        return res

class Solution(object):
    def distanceK(self, root, target, K):
        if K == 0:
            return [target.val]

        def gather(nd, depth, ans):
            if nd is None or depth < 0:
                return
            if depth == 0:
                ans.append(nd.val)
                return
            gather(nd.left, depth - 1, ans)
            gather(nd.right, depth - 1, ans)

        ans = []
        gather(target.left, K - 1, ans)
        gather(target.right, K - 1, ans)

        route = []
        def trace(nd, goal):
            if nd is None:
                return False
            route.append(nd)
            if nd == goal:
                return True
            if trace(nd.left, goal) or trace(nd.right, goal):
                return True
            route.pop()
            return False

        trace(root, target, route)

        for idx in range(len(route) - 2, -1, -1):
            steps_up = len(route) - 1 - idx
            if steps_up > K:
                continue
            leftover = K - steps_up
            parent_node = route[idx]
            if leftover == 0:
                ans.append(parent_node.val)
                continue
            path_kid = route[idx + 1]
            for kid in (parent_node.left, parent_node.right):
                if kid is not None and kid != path_kid:
                    gather(kid, leftover - 1, ans)
        return ans

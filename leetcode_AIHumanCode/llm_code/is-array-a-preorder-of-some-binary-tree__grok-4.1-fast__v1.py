class Solution(object):
    def isPreorder(self, node_pairs):
        if not node_pairs:
            return False
        active_path = [node_pairs[0][0]]
        for j in range(1, len(node_pairs)):
            target_parent = node_pairs[j][1]
            while active_path and active_path[-1] != target_parent:
                active_path.pop()
            if not active_path:
                return False
            active_path.append(node_pairs[j][0])
        return True

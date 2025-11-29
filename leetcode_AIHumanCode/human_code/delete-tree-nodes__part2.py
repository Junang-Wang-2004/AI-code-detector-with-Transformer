# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        """
        # assuming parent[i] < i for all i > 0
        result = [1]*nodes
        for i in reversed(range(1, nodes)):
            value[parent[i]] += value[i]
            result[parent[i]] += result[i] if value[i] else 0
        return result[0]

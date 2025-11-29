# Time:  O(n)
# Space: O(w), w is the max number of nodes in the levels of the tree
class Solution2(object):
    def getImportance(self, employees, id):
        """
        """
        result, q = 0, collections.deque([id])
        while q:
            curr = q.popleft()
            employee = employees[curr-1]
            result += employee.importance
            for id in employee.subordinates:
                q.append(id)
        return result


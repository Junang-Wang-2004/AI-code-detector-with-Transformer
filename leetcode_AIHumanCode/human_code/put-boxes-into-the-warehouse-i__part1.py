# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        """
        boxes.sort(reverse=True)
        result = 0
        for h in boxes:
            if h > warehouse[result]:
                continue
            result += 1
            if result == len(warehouse):
                break
        return result



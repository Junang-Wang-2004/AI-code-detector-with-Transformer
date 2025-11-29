class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        curr = head
        while curr and top <= bottom and left <= right:
            for c in range(left, right + 1):
                if not curr:
                    break
                matrix[top][c] = curr.val
                curr = curr.next
            top += 1
            for r in range(top, bottom + 1):
                if not curr:
                    break
                matrix[r][right] = curr.val
                curr = curr.next
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    if not curr:
                        break
                    matrix[bottom][c] = curr.val
                    curr = curr.next
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    if not curr:
                        break
                    matrix[r][left] = curr.val
                    curr = curr.next
                left += 1
        return matrix

class Solution:
    def splitListToParts(self, head, k):
        size = 0
        temp = head
        while temp is not None:
            size += 1
            temp = temp.next
        q = size // k
        r = size % k
        parts = []
        temp = head
        for i in range(k):
            parts.append(temp)
            steps = q + (1 if i < r else 0) - 1
            for _ in range(steps):
                if temp is None:
                    break
                temp = temp.next
            if temp is not None:
                nxt = temp.next
                temp.next = None
                temp = nxt
        return parts

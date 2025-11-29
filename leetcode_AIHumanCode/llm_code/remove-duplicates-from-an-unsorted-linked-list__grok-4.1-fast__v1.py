class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        freq = {}
        probe = head
        while probe:
            v = probe.val
            freq[v] = freq.get(v, 0) + 1
            probe = probe.next
        uniques = []
        probe = head
        while probe:
            if freq[probe.val] == 1:
                uniques.append(probe)
            probe = probe.next
        if not uniques:
            return None
        for idx in range(len(uniques) - 1):
            uniques[idx].next = uniques[idx + 1]
        uniques[-1].next = None
        return uniques[0]

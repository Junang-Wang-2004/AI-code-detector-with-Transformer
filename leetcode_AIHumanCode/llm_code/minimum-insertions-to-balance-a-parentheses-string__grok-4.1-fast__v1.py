class Solution(object):
    def minInsertions(self, s):
        unmatched = 0
        pending_opens = 0
        for symbol in s:
            if symbol == '(':
                pending_opens += 1
            else:
                if pending_opens == 0:
                    unmatched += 1
                else:
                    pending_opens -= 1
        return unmatched + pending_opens

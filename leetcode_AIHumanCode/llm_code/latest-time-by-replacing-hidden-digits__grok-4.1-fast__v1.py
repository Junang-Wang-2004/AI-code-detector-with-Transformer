class Solution:
    def maximumTime(self, time):
        tm = list(time)
        if tm[0] == '?':
            if tm[1] == '?' or '0' <= tm[1] <= '3':
                tm[0] = '2'
            else:
                tm[0] = '1'
        if tm[1] == '?':
            tm[1] = '3' if tm[0] == '2' else '9'
        if tm[3] == '?':
            tm[3] = '5'
        if tm[4] == '?':
            tm[4] = '9'
        return ''.join(tm)

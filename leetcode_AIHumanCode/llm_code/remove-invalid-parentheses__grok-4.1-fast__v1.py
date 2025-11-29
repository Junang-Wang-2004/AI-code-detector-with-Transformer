class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(st):
            cnt = 0
            for ch in st:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        from collections import deque
        q = deque([s])
        seen = {s}
        while q:
            sz = len(q)
            valids = []
            for _ in range(sz):
                cur = q.popleft()
                if is_valid(cur):
                    valids.append(cur)
                    continue
                for i in range(len(cur)):
                    if cur[i] not in '()':
                        continue
                    if i > 0 and cur[i] == cur[i-1]:
                        continue
                    nxt = cur[:i] + cur[i+1:]
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)
            if valids:
                return valids
        return []

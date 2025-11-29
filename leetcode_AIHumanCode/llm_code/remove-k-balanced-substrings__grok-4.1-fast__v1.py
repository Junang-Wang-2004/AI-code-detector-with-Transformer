class Solution:
    def removeSubstring(self, s, k):
        stack = []
        tracker = [0]
        full = 2 * k
        for c in s:
            stack.append(c)
            if c == '(':
                if tracker[0] < k:
                    tracker[0] += 1
                elif tracker[0] > k:
                    tracker[0] = 1
            else:
                if tracker[0] >= k:
                    tracker[0] += 1
                else:
                    tracker[0] = 0
            if tracker[0] == full:
                for _ in range(full):
                    stack.pop()
                tracker[0] = 0
                check_start = max(0, len(stack) - full + 1)
                for idx in range(check_start, len(stack)):
                    ch = stack[idx]
                    if ch == '(':
                        if tracker[0] < k:
                            tracker[0] += 1
                        elif tracker[0] > k:
                            tracker[0] = 1
                    else:
                        if tracker[0] >= k:
                            tracker[0] += 1
                        else:
                            tracker[0] = 0
        return ''.join(stack)

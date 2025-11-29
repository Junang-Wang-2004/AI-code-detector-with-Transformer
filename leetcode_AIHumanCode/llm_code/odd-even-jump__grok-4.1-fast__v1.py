class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        next_odd = [None] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and A[stack[-1]] < A[i]:
                stack.pop()
            if stack:
                next_odd[i] = stack[-1]
            stack.append(i)

        next_greater = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(i)

        next_even = [None] * n
        for i in range(n):
            cand = next_greater[i] - 1
            if cand > i:
                next_even[i] = cand

        can_start_odd = [False] * n
        can_start_even = [False] * n
        can_start_odd[n - 1] = True
        can_start_even[n - 1] = True
        for i in range(n - 2, -1, -1):
            if next_odd[i] is not None:
                can_start_odd[i] = can_start_even[next_odd[i]]
            if next_even[i] is not None:
                can_start_even[i] = can_start_odd[next_even[i]]
        return sum(can_start_odd)

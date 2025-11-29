class Solution:
    def maximumStrongPairXor(self, nums):
        nums.sort()
        if not nums:
            return 0
        BITS = nums[-1].bit_length()
        NODES = 3200010
        nodes = [[-1] * 2 for _ in range(NODES)]
        counts = [0] * NODES
        node_id = 1

        def alloc():
            nonlocal node_id
            res = node_id
            node_id += 1
            return res

        def insert(val, sign):
            nonlocal node_id
            pos = 0
            for k in range(BITS - 1, -1, -1):
                b = (val >> k) & 1
                if nodes[pos][b] == -1:
                    nodes[pos][b] = alloc()
                pos = nodes[pos][b]
                counts[pos] += sign

        def find_max(val):
            pos = 0
            mx_xor = 0
            for k in range(BITS - 1, -1, -1):
                b = (val >> k) & 1
                opp = 1 - b
                nxt = nodes[pos][opp]
                if nxt != -1 and counts[nxt] > 0:
                    mx_xor |= (1 << k)
                    pos = nxt
                else:
                    nxt = nodes[pos][b]
                    if nxt == -1:
                        break
                    pos = nxt
            return mx_xor

        left = 0
        answer = 0
        for right in range(len(nums)):
            insert(nums[right], 1)
            while left <= right and nums[right] > 2 * nums[left]:
                insert(nums[left], -1)
                left += 1
            answer = max(answer, find_max(nums[right]))
        return answer

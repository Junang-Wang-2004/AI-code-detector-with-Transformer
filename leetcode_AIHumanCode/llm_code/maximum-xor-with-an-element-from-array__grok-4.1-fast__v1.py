class Trie:
    def __init__(self, bits):
        self.bits = bits
        self.nodes = [[-1, -1]]
        self.next_node = 1

    def add(self, val):
        cur = 0
        for k in range(self.bits - 1, -1, -1):
            b = (val >> k) & 1
            if self.nodes[cur][b] == -1:
                self.nodes[cur][b] = self.next_node
                self.nodes.append([-1, -1])
                self.next_node += 1
            cur = self.nodes[cur][b]

    def find_max_xor(self, val):
        if self.nodes[0][0] == -1 and self.nodes[0][1] == -1:
            return -1
        cur = 0
        xor_val = 0
        for k in range(self.bits - 1, -1, -1):
            b = (val >> k) & 1
            opp_b = 1 - b
            if self.nodes[cur][opp_b] != -1:
                xor_val |= (1 << k)
                cur = self.nodes[cur][opp_b]
            else:
                cur = self.nodes[cur][b]
        return xor_val


class Solution:
    def maximizeXor(self, arr, qs):
        arr.sort()
        if not arr:
            return [-1] * len(qs)
        max_num = max(arr[-1], max(q[0] for q in qs))
        bit_cnt = max_num.bit_length()
        indexed_qs = sorted(enumerate(qs), key=lambda e: e[1][1])
        bt = Trie(bit_cnt)
        output = [-1] * len(qs)
        pos = 0
        for orig_idx, (target, limit) in indexed_qs:
            while pos < len(arr) and arr[pos] <= limit:
                bt.add(arr[pos])
                pos += 1
            output[orig_idx] = bt.find_max_xor(target)
        return output

class TreeAncestor:
    def __init__(self, n, parent):
        LOG = 20
        self.jump = [[-1] * LOG for _ in range(n)]
        for i in range(n):
            if parent[i] != -1:
                self.jump[i][0] = parent[i]
        for lv in range(1, LOG):
            for i in range(n):
                prev = self.jump[i][lv - 1]
                if prev != -1:
                    self.jump[i][lv] = self.jump[prev][lv - 1]

    def getKthAncestor(self, node, k):
        for bit in range(20):
            if k & (1 << bit):
                if self.jump[node][bit] == -1:
                    return -1
                node = self.jump[node][bit]
        return node

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size_rank = [0] * size

    def find(self, idx):
        root = idx
        while self.parent[root] != root:
            root = self.parent[root]
        cur = idx
        while cur != root:
            nxt = self.parent[cur]
            self.parent[cur] = root
            cur = nxt
        return root

    def unite(self, idx1, idx2):
        r1 = self.find(idx1)
        r2 = self.find(idx2)
        if r1 == r2:
            return False
        if self.size_rank[r1] < self.size_rank[r2]:
            self.parent[r1] = r2
        elif self.size_rank[r1] > self.size_rank[r2]:
            self.parent[r2] = r1
        else:
            self.parent[r2] = r1
            self.size_rank[r1] += 1
        return True


class DistanceLimitedPathsExist:
    def __init__(self, nodes, connections):
        self.node_count = nodes
        self.graph = [[] for _ in range(nodes)]
        self.components = UnionFind(nodes)
        sorted_connections = sorted(connections, key=lambda conn: conn[2])
        for u, v, wt in sorted_connections:
            if self.components.unite(u, v):
                self.graph[u].append((v, wt))
                self.graph[v].append((u, wt))
        LOG_LEVELS = 14
        self.ancestor_table = [[-1] * nodes for _ in range(LOG_LEVELS)]
        self.edge_max_table = [[0] * nodes for _ in range(LOG_LEVELS)]
        self.node_depths = [0] * nodes
        self.explored = [False] * nodes
        self._build_level_zero()
        self._build_higher_levels(LOG_LEVELS)

    def _build_level_zero(self):
        traversal_stack = []
        for start_node in range(self.node_count):
            if self.explored[start_node]:
                continue
            traversal_stack.append((start_node, -1, 0, 0))
            while traversal_stack:
                current, prev, level, prev_weight = traversal_stack[-1]
                if not self.explored[current]:
                    self.explored[current] = True
                    self.ancestor_table[0][current] = prev
                    self.node_depths[current] = level
                    self.edge_max_table[0][current] = prev_weight
                    for neighbor, weight in self.graph[current]:
                        if neighbor != prev:
                            traversal_stack.append((neighbor, current, level + 1, weight))
                else:
                    traversal_stack.pop()

    def _build_higher_levels(self, log_size):
        for level in range(1, log_size):
            for current in range(self.node_count):
                direct_anc = self.ancestor_table[level - 1][current]
                if direct_anc != -1:
                    self.ancestor_table[level][current] = self.ancestor_table[level - 1][direct_anc]
                    self.edge_max_table[level][current] = max(
                        self.edge_max_table[level - 1][current],
                        self.edge_max_table[level - 1][direct_anc]
                    )

    def _climb_up(self, start, steps):
        current_max = 0
        level = 0
        while steps > 0:
            if steps & 1:
                current_max = max(current_max, self.edge_max_table[level][start])
                start = self.ancestor_table[level][start]
            steps >>= 1
            level += 1
        return start, current_max

    def query(self, start, end, max_weight):
        if self.components.find(start) != self.components.find(end):
            return False
        u, v = start, end
        path_max = 0
        if self.node_depths[u] > self.node_depths[v]:
            u, v = v, u
        depth_diff = self.node_depths[v] - self.node_depths[u]
        v, climb_max = self._climb_up(v, depth_diff)
        path_max = max(path_max, climb_max)
        if u == v:
            return path_max < max_weight
        for level in range(13, -1, -1):
            if (self.ancestor_table[level][u] != self.ancestor_table[level][v] and
                self.ancestor_table[level][u] != -1):
                path_max = max(path_max, self.edge_max_table[level][u],
                               self.edge_max_table[level][v])
                u = self.ancestor_table[level][u]
                v = self.ancestor_table[level][v]
        path_max = max(path_max, self.edge_max_table[0][u],
                       self.edge_max_table[

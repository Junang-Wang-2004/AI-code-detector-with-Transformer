class Solution:
    def maximumInvitations(self, grid):
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        def build_graph(left_size, right_size, is_row_left):
            graph = {}
            for left in range(left_size):
                neighbors = []
                for right in range(right_size):
                    if (grid[left][right] if is_row_left else grid[right][left]):
                        neighbors.append(right)
                graph[left] = neighbors
            return graph
        
        if rows <= cols:
            adj_list = build_graph(rows, cols, True)
            left_n = rows
            right_n = cols
        else:
            adj_list = build_graph(cols, rows, False)
            left_n = cols
            right_n = rows
        
        pair_left = [-1] * left_n
        pair_right = [-1] * right_n
        
        def find_path(node, seen):
            for neigh in adj_list[node]:
                if seen[neigh]:
                    continue
                seen[neigh] = True
                if pair_right[neigh] == -1 or find_path(pair_right[neigh], seen):
                    pair_left[node] = neigh
                    pair_right[neigh] = node
                    return True
            return False
        
        total_matches = 0
        for left_node in range(left_n):
            if pair_left[left_node] == -1:
                seen = [False] * right_n
                if find_path(left_node, seen):
                    total_matches += 1
        
        return total_matches

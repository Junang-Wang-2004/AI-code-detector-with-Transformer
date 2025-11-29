class Solution:
    def maxStudents(self, seats):
        m = len(seats)
        if m == 0:
            return 0
        n = len(seats[0])
        total_empty = sum(s.count('.') for s in seats)
        
        even_pos = []
        odd_pos = []
        even_id = {}
        odd_id = {}
        eidx = 0
        oidx = 0
        for r in range(m):
            for c in range(n):
                if seats[r][c] == '.':
                    if c % 2 == 0:
                        even_pos.append((r, c))
                        even_id[(r, c)] = eidx
                        eidx += 1
                    else:
                        odd_pos.append((r, c))
                        odd_id[(r, c)] = oidx
                        oidx += 1
        
        num_even = len(even_pos)
        num_odd = len(odd_pos)
        
        graph = [[] for _ in range(num_even)]
        deltas = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]
        for ei in range(num_even):
            row, col = even_pos[ei]
            for dr, dc in deltas:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and seats[nr][nc] == '.' and nc % 2 == 1:
                    if (nr, nc) in odd_id:
                        graph[ei].append(odd_id[(nr, nc)])
        
        mate_odd = [-1] * num_odd
        mate_even = [-1] * num_even
        visited = [False] * num_odd
        
        def find_path(ei):
            for oi in graph[ei]:
                if visited[oi]:
                    continue
                visited[oi] = True
                if mate_odd[oi] == -1 or find_path(mate_odd[oi]):
                    mate_odd[oi] = ei
                    mate_even[ei] = oi
                    return True
            return False
        
        max_match = 0
        for ei in range(num_even):
            if mate_even[ei] == -1:
                visited = [False] * num_odd
                if find_path(ei):
                    max_match += 1
        
        return total_empty - max_match

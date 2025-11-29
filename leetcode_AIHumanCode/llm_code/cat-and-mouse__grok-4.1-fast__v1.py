from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        color = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        deg = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        hole_neigh = set(graph[0])
        MOUSE_TURN, CAT_TURN = 0, 1
        for mouse_pos in range(n):
            for cat_pos in range(n):
                deg[mouse_pos][cat_pos][MOUSE_TURN] = len(graph[mouse_pos])
                cdeg = len(graph[cat_pos])
                if cat_pos in hole_neigh:
                    cdeg -= 1
                deg[mouse_pos][cat_pos][CAT_TURN] = cdeg
        q = deque()
        for cat_pos in range(1, n):
            color[0][cat_pos][CAT_TURN] = 1
            q.append((0, cat_pos, CAT_TURN))
        for pos in range(1, n):
            color[pos][pos][MOUSE_TURN] = 2
            q.append((pos, pos, MOUSE_TURN))
            color[pos][pos][CAT_TURN] = 2
            q.append((pos, pos, CAT_TURN))
        while q:
            m_pos, c_pos, turn = q.popleft()
            win = color[m_pos][c_pos][turn]
            if turn == CAT_TURN:
                for p_mouse in graph[m_pos]:
                    p_m, p_c, p_t = p_mouse, c_pos, MOUSE_TURN
                    if color[p_m][p_c][p_t] != 0:
                        continue
                    if p_t == win:
                        color[p_m][p_c][p_t] = win
                        q.append((p_m, p_c, p_t))
                    else:
                        deg[p_m][p_c][p_t] -= 1
                        if deg[p_m][p_c][p_t] == 0:
                            color[p_m][p_c][p_t] = win
                            q.append((p_m, p_c, p_t))
            else:
                for p_cat in graph[c_pos]:
                    if p_cat == 0:
                        continue
                    p_m, p_c, p_t = m_pos, p_cat, CAT_TURN
                    if color[p_m][p_c][p_t] != 0:
                        continue
                    if p_t == win:
                        color[p_m][p_c][p_t] = win
                        q.append((p_m, p_c, p_t))
                    else:
                        deg[p_m][p_c][p_t] -= 1
                        if deg[p_m][p_c][p_t] == 0:
                            color[p_m][p_c][p_t] = win
                            q.append((p_m, p_c, p_t))
        return color[1][2][MOUSE_TURN]

from collections import deque

class C1(object):

    def __init__(self, a1, a2, a3):
        self.board_width = a1
        self.board_height = a2
        self.food_positions = [(r, c) for v1, v2 in a3]
        self.current_food_index = 0
        self.game_score = 0
        self.snake = deque([(0, 0)])
        self.filled_cells = set([(0, 0)])
        self.direction_vectors = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def move(self, a1):
        v1 = self.snake[-1]
        v2, v3 = self.direction_vectors[a1]
        v4 = v1[0] + v2
        v5 = v1[1] + v3
        v6 = self.snake.popleft()
        self.filled_cells.remove(v6)
        if v4 < 0 or v4 >= self.board_height or v5 < 0 or (v5 >= self.board_width) or ((v4, v5) in self.filled_cells):
            return -1
        v7 = False
        if self.current_food_index < len(self.food_positions) and self.food_positions[self.current_food_index] == (v4, v5):
            v7 = True
            self.game_score += 1
            self.current_food_index += 1
            self.snake.appendleft(v6)
            self.filled_cells.add(v6)
        self.snake.append((v4, v5))
        self.filled_cells.add((v4, v5))
        return self.game_score

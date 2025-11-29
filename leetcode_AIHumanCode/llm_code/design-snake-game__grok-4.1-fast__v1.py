from collections import deque

class SnakeGame(object):

    def __init__(self, width, height, food):
        self.board_width = width
        self.board_height = height
        self.food_positions = [(r, c) for r, c in food]
        self.current_food_index = 0
        self.game_score = 0
        self.snake = deque([(0, 0)])
        self.filled_cells = set([(0, 0)])
        self.direction_vectors = {
            "U": (-1, 0),
            "L": (0, -1),
            "R": (0, 1),
            "D": (1, 0)
        }

    def move(self, move_dir):
        head_pos = self.snake[-1]
        d_row, d_col = self.direction_vectors[move_dir]
        next_row = head_pos[0] + d_row
        next_col = head_pos[1] + d_col
        prev_tail = self.snake.popleft()
        self.filled_cells.remove(prev_tail)
        if (next_row < 0 or next_row >= self.board_height or
            next_col < 0 or next_col >= self.board_width or
            (next_row, next_col) in self.filled_cells):
            return -1
        food_eaten = False
        if (self.current_food_index < len(self.food_positions) and
            self.food_positions[self.current_food_index] == (next_row, next_col)):
            food_eaten = True
            self.game_score += 1
            self.current_food_index += 1
            self.snake.appendleft(prev_tail)
            self.filled_cells.add(prev_tail)
        self.snake.append((next_row, next_col))
        self.filled_cells.add((next_row, next_col))
        return self.game_score

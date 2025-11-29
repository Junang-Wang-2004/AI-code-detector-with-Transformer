import collections

class MaxStack:

    def __init__(self):
        self.position_map = {}
        self.value_positions = collections.defaultdict(list)
        self.next_position = 0
        self.top_position = None
        self.current_maximum = None

    def push(self, x):
        position = self.next_position
        self.next_position += 1
        self.position_map[position] = x
        self.value_positions[x].append(position)
        self.top_position = position
        if self.current_maximum is None or x > self.current_maximum:
            self.current_maximum = x

    def pop(self):
        value = self.position_map[self.top_position]
        self._eliminate_top_occurrence(value)
        return value

    def top(self):
        return self.position_map[self.top_position]

    def peekMax(self):
        return self.current_maximum

    def popMax(self):
        value = self.current_maximum
        self._eliminate_top_occurrence(value)
        return value

    def _eliminate_top_occurrence(self, value):
        positions = self.value_positions[value]
        position = positions.pop()
        del self.position_map[position]
        if not positions:
            del self.value_positions[value]
        if position == self.top_position:
            self.top_position = max(self.position_map.keys()) if self.position_map else None
        if value == self.current_maximum and value not in self.value_positions:
            self.current_maximum = max(self.value_positions.keys()) if self.value_positions else None

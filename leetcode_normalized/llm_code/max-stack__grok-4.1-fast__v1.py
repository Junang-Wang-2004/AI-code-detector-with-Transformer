import collections

class C1:

    def __init__(self):
        self.position_map = {}
        self.value_positions = collections.defaultdict(list)
        self.next_position = 0
        self.top_position = None
        self.current_maximum = None

    def push(self, a1):
        v1 = self.next_position
        self.next_position += 1
        self.position_map[v1] = a1
        self.value_positions[a1].append(v1)
        self.top_position = v1
        if self.current_maximum is None or a1 > self.current_maximum:
            self.current_maximum = a1

    def pop(self):
        v1 = self.position_map[self.top_position]
        self._eliminate_top_occurrence(v1)
        return v1

    def top(self):
        return self.position_map[self.top_position]

    def peekMax(self):
        return self.current_maximum

    def popMax(self):
        v1 = self.current_maximum
        self._eliminate_top_occurrence(v1)
        return v1

    def _eliminate_top_occurrence(self, a1):
        v1 = self.value_positions[a1]
        v2 = v1.pop()
        del self.position_map[v2]
        if not v1:
            del self.value_positions[a1]
        if v2 == self.top_position:
            self.top_position = max(self.position_map.keys()) if self.position_map else None
        if a1 == self.current_maximum and a1 not in self.value_positions:
            self.current_maximum = max(self.value_positions.keys()) if self.value_positions else None

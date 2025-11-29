import heapq

class ExamRoom(object):

    def __init__(self, N):
        self.N = N
        self.prev_neighbor = {N: -1}
        self.next_neighbor = {-1: N}
        self.maxgaps = []
        heapq.heappush(self.maxgaps, (-(N), -1, N))

    def _gap_size(self, left, right):
        if left == -1 or right == self.N:
            return right - left - 1
        return (right - left) // 2

    def seat(self):
        while self.maxgaps and not (
            self.next_neighbor[self.maxgaps[0][1]] == self.maxgaps[0][2]
            and self.prev_neighbor[self.maxgaps[0][2]] == self.maxgaps[0][1]
        ):
            heapq.heappop(self.maxgaps)
        _, left_end, right_end = heapq.heappop(self.maxgaps)
        if left_end == -1:
            new_seat = 0
        elif right_end == self.N:
            new_seat = self.N - 1
        else:
            new_seat = (left_end + right_end) // 2
        self.prev_neighbor[new_seat] = left_end
        self.next_neighbor[new_seat] = right_end
        self.next_neighbor[left_end] = new_seat
        self.prev_neighbor[right_end] = new_seat
        heapq.heappush(self.maxgaps, (-self._gap_size(left_end, new_seat), left_end, new_seat))
        heapq.heappush(self.maxgaps, (-self._gap_size(new_seat, right_end), new_seat, right_end))
        return new_seat

    def leave(self, pos):
        left_end = self.prev_neighbor[pos]
        right_end = self.next_neighbor[pos]
        self.next_neighbor[left_end] = right_end
        self.prev_neighbor[right_end] = left_end
        del self.prev_neighbor[pos]
        del self.next_neighbor[pos]
        heapq.heappush(self.maxgaps, (-self._gap_size(left_end, right_end), left_end, right_end))

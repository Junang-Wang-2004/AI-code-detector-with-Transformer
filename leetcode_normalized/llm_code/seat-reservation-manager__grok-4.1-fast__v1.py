import heapq

class C1:

    def __init__(self, a1: int):
        self.free_seats = [seat_num for v1 in range(1, a1 + 1)]
        heapq.heapify(self.free_seats)

    def reserve(self) -> int:
        return heapq.heappop(self.free_seats)

    def unreserve(self, a1: int) -> None:
        heapq.heappush(self.free_seats, a1)

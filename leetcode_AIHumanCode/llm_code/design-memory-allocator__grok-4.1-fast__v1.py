from sortedcontainers import SortedList
import collections

class Allocator:
    def __init__(self, n):
        self.free_slots = SortedList()
        self.free_slots.add([0, n])
        self.allocations = collections.defaultdict(list)

    def allocate(self, size, mID):
        for slot in self.free_slots:
            begin = slot[0]
            length = slot[1]
            if length >= size:
                self.free_slots.remove([begin, length])
                self.allocations[mID].append([begin, size])
                if length > size:
                    self.free_slots.add([begin + size, length - size])
                return begin
        return -1

    def free(self, mID):
        allocation_list = self.allocations.get(mID, [])
        if not allocation_list:
            return 0
        sorted_allocs = sorted(allocation_list, key=lambda x: x[0])
        merged = []
        for b, l in sorted_allocs:
            if merged and merged[-1][0] + merged[-1][1] == b:
                merged[-1][1] += l
            else:
                merged.append([b, l])
        total_freed = sum(l for _, l in merged)
        del self.allocations[mID]
        for new_slot in merged:
            self.free_slots.add(new_slot)
            idx = self.free_slots.bisect_left(new_slot)
            if idx + 1 < len(self.free_slots) and self.free_slots[idx][0] + self.free_slots[idx][1] == self.free_slots[idx + 1][0]:
                self.free_slots[idx][1] += self.free_slots[idx + 1][1]
                del self.free_slots[idx + 1]
            if idx > 0 and self.free_slots[idx - 1][0] + self.free_slots[idx - 1][1] == self.free_slots[idx][0]:
                self.free_slots[idx - 1][1] += self.free_slots[idx][1]
                del self.free_slots[idx]
        return total_freed

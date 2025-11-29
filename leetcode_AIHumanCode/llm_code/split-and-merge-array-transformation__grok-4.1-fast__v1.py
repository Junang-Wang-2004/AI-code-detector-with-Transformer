class Solution:
    def minSplitMerge(self, nums1, nums2):
        source = tuple(nums1)
        target = tuple(nums2)
        if source == target:
            return 0
        
        from collections import deque
        queue = deque([source])
        distances = {source: 0}
        
        while queue:
            current = queue.popleft()
            level = distances[current]
            for candidate in self._generate_moves(current):
                if candidate == target:
                    return level + 1
                if candidate not in distances:
                    distances[candidate] = level + 1
                    queue.append(candidate)
        return -1
    
    def _generate_moves(self, sequence):
        size = len(sequence)
        for start_idx in range(size):
            for stop_idx in range(start_idx, size):
                excerpt = sequence[start_idx:stop_idx + 1]
                residue = sequence[:start_idx] + sequence[stop_idx + 1:]
                pos_size = len(residue)
                for placement in range(pos_size + 1):
                    if placement == start_idx:
                        continue
                    reformed = residue[:placement] + excerpt + residue[placement:]
                    yield reformed

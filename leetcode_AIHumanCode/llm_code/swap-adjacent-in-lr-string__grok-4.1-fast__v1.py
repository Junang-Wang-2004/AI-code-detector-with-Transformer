class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        seq_start = ''.join(c for c in start if c != 'X')
        seq_end = ''.join(c for c in end if c != 'X')
        if seq_start != seq_end:
            return False
        
        start_positions = [idx for idx, c in enumerate(start) if c != 'X']
        end_positions = [idx for idx, c in enumerate(end) if c != 'X']
        
        num_moves = len(start_positions)
        for k in range(num_moves):
            if seq_start[k] == 'L' and start_positions[k] < end_positions[k]:
                return False
            if seq_start[k] == 'R' and start_positions[k] > end_positions[k]:
                return False
        
        return True

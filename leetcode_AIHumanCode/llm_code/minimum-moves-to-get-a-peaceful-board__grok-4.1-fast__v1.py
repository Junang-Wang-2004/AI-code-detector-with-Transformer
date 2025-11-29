class Solution:
    def minMoves(self, rooks):
        row_coords = [pos[0] for pos in rooks]
        col_coords = [pos[1] for pos in rooks]
        
        def total_cost(coord_list):
            sorted_list = sorted(coord_list)
            return sum(abs(sorted_list[i] - i) for i in range(len(sorted_list)))
        
        return total_cost(row_coords) + total_cost(col_coords)

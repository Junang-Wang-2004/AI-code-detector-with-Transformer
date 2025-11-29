class Solution:
    def findRadius(self, house_positions, heater_positions):
        house_positions.sort()
        heater_positions.sort()
        max_r = 0
        heater_idx = 0
        num_heaters = len(heater_positions)
        for position in house_positions:
            while heater_idx < num_heaters and heater_positions[heater_idx] < position:
                heater_idx += 1
            dist_next = float('inf') if heater_idx == num_heaters else heater_positions[heater_idx] - position
            dist_prev = float('inf') if heater_idx == 0 else position - heater_positions[heater_idx - 1]
            closest_dist = min(dist_next, dist_prev)
            max_r = max(max_r, closest_dist)
        return max_r

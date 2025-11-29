class Solution:
    def getCollisionTimes(self, cars):
        res = [-1.0] * len(cars)
        candidates = []
        for idx in range(len(cars) - 1, -1, -1):
            position, velocity = cars[idx]
            while candidates:
                f_pos, f_vel, f_time = candidates[-1]
                if f_vel >= velocity:
                    candidates.pop()
                    continue
                coll_t = (f_pos - position) / (velocity - f_vel)
                if 0 < f_time <= coll_t:
                    candidates.pop()
                else:
                    break
            if candidates:
                res[idx] = (candidates[-1][0] - position) / (velocity - candidates[-1][1])
            candidates.append((position, velocity, res[idx]))
        return res

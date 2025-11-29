class MountainArray(object):
   def get(self, index):
       """
       """
       pass

   def length(self):
       """
       """
       pass


class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        sz = mountain_arr.length()
        i, j = 0, sz - 1
        while i < j:
            k = (i + j) // 2
            if mountain_arr.get(k) < mountain_arr.get(k + 1):
                i = k + 1
            else:
                j = k
        peak_idx = i
        l, r = 0, peak_idx
        while l < r:
            m_idx = l + (r - l) // 2
            if mountain_arr.get(m_idx) < target:
                l = m_idx + 1
            else:
                r = m_idx
        candidate = l
        if candidate <= peak_idx and mountain_arr.get(candidate) == target:
            return candidate
        l, r = peak_idx, sz - 1
        while l < r:
            m_idx = l + (r - l) // 2
            if mountain_arr.get(m_idx) > target:
                l = m_idx + 1
            else:
                r = m_idx
        candidate = l
        if candidate < sz and mountain_arr.get(candidate) == target:
            return candidate
        return -1

class ArrayReader(object):
   def compareSub(self, l, r, x, y):
       pass

   def length(self):
       pass

class Solution(object):
    def getIndex(self, reader):
        beg, fin = 0, reader.length() - 1
        while beg < fin:
            segsize = fin - beg + 1
            hsize = (segsize + 1) // 2
            l_end = beg + hsize - 1
            r_beg = fin - hsize + 1
            if reader.compareSub(beg, l_end, r_beg, fin) >= 0:
                fin = l_end
            else:
                beg = l_end + 1
        return beg

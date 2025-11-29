# Time:  O(1)
# Space: O(1)
class Solution2(object):
    def minimumPerimeter(self, neededApples):
        """
        """
        # r+r    , (r-1)+r, ..., 1+r, 0+r    , 1+r, ..., (r-1)+r, r+r
        # r+(r-1),                    0+(r-1),                    r+(r-1)
        #  .                           .                           .    
        #  .                           .                           .    
        #  .                           .                           .    
        # r+1    , (r-1)+1, ..., 1+1, 1+0    , 1+1, ..., (r-1)+1, r+1
        # r+0    , (r-1)+0, ..., 1+0, 0+0    , 1+0, ..., (r-1)+0, r+0
        # r+1    , (r-1)+1, ..., 1+1, 1+0    , 1+1, ..., (r-1)+1, r+1
        #  .                           .                           .    
        #  .                           .                           .    
        #  .                           .                           .       
        # r+(r-1),                    0+(r-1),                    r+(r-1)
        # r+r    , (r-1)+r, ..., 1+r, 0+r    , 1+r, ..., r+(r-1), r+r
        #
        # each up/down direction forms an arithmetic sequence, there are 2r+1 columns
        # => 2*(1+r)*r/2 * (2r+1)
        #
        # each left/right direction forms an arithmetic sequence, there are 2r+1 rows
        # => 2*(1+r)*r/2 * (2r+1)
        #
        # => total = 2 * 2*(1+r)*r/2 * (2r+1) = r*(2r+1)*(2r+2) = 4r^3+6r^2+2r
        # => find min r, s.t. (2r)(2r+1)*(2r+2) >= 2*neededApples
        # => find min x = 2r+2, s.t. (x-2)(x-1)(x) >= 2*neededApples

        x = int((2*neededApples)**(1.0/3))
        x -= x%2
        assert((x-2)*(x-1)*x < 2*neededApples < (x+2)**3)
        x += 2
        if (x-2)*(x-1)*x < 2*neededApples:
            x += 2
        return 8*(x-2)//2



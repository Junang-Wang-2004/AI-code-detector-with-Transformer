# Time:  O(1)
# Space: O(1)

import math


class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        """
        # find min r, s.t. 4r^3+6r^2+2r-neededApples >= 0
        # => by depressed cubic (https://en.wikipedia.org/wiki/Cubic_equation#Depressed_cubic)
        #    let x = r+(6/(3*4)), r = x-(1/2)
        #    4(x-(1/2))^3+6(x-(1/2))^2+2(x-(1/2))-neededApples
        #    = 4(x^3-3/2x^2+3/4x-1/8)
        #      + 6(x^2-x+1/4)
        #      + 2(x-1/2)
        #    = 4x^3-x-neededApples >= 0
        #
        # find x, s.t. 4x^3-x-neededApples = 0 <=> x^3+(-1/4)x+(-neededApples/4) = 0
        # => by Cardano's formula (https://en.wikipedia.org/wiki/Cubic_equation#Cardano's_formula)
        #    x^3 + px + q = 0, p = (-1/4), q = (-neededApples/4)
        #    since (q/2)^2+(p/3)^3 = neededApples^2/64-1/1728 > 0 => only one real root
        #    => x = (-q/2 + ((q/2)^2+(p/3)^3)^(1/2)) + (-q/2 - ((q/2)^2+(p/3)^3)^(1/2))
        #       r = x-(1/2)
        # => min r = ceil(r)

        a, b, c, d = 4.0, 6.0, 2.0, float(-neededApples)
        p = (3*a*c-b**2)/(3*a**2)  # -1/4.0
        q = (2*b**3-9*a*b*c+27*a**2*d)/(27*a**3)  # -neededApples/4.0
        assert((q/2)**2+(p/3)**3 > 0)  # case of only one real root
        x = (-q/2 + ((q/2)**2+(p/3)**3)**0.5)**(1.0/3) + \
            (-q/2 - ((q/2)**2+(p/3)**3)**0.5)**(1.0/3)
        return 8*int(math.ceil(x - b/(3*a)))
                             


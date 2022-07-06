class Solution(object):
    def binPaw(self, a, b):
        if b == 0:
            return 1

        if b % 2:
            return a * self.binPaw(a, b - 1) 
        b = self.binPaw(a, b / 2)
        return b * b

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lf, rg = 0, x
        while lf < rg:
            md = (lf + rg) // 2
            if md * md > x:
                rg = md - 1
            else:
                lf = md + 1
        if lf * lf > x:
            return lf - 1 
        return lf


def main():
    print(Solution().mySqrt(1023))
        
main()
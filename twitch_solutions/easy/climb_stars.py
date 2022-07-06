class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        cur = 0
        while n > 0:
            new_prev = cur
            cur += prev
            prev = new_prev
            n -= 1
            print("{}:{}".format(n, cur))
        return cur

Solution().climbStairs(10)

        
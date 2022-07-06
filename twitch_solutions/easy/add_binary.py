class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        mem = 0
        res = []
        for i in range(min(len(a), len(b))):
            digit_res = mem + int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) 
            res.append(str(digit_res % 2))
            mem = int(digit_res / 10)
        if mem:
            res.append(mem)
        return "".join(reversed(res))
            



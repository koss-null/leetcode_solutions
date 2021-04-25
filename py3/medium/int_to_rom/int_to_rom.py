import collections


class Solution:
    table = collections.OrderedDict()

    def __init__(self):
        self.table["I"] = 1
        self.table["IV"] = 4
        self.table["V"] = 5
        self.table["IX"] = 9
        self.table["X"] = 10
        self.table["XL"] = 40
        self.table["L"] = 50
        self.table["XC"] = 9
        self.table["X"] = 10
        self.table["XC"] = 90
        self.table["C"] = 100
        self.table["CD"] = 400
        self.table["D"] = 500
        self.table["CM"] = 900
        self.table["M"] = 1000

    def intToRoman(self, num: int) -> str:
        res = []
        vals = list(self.table.keys())
        idx = len(vals) - 1
        while num:
            if num - self.table[vals[idx]] >= 0:
                num -= self.table[vals[idx]]
                res.append(vals[idx])
            else:
                idx -= 1
        return "".join(res)





def main(a):
    return Solution().intToRoman(a)


def get_input(inp):
    return int(inp)


def format_output(a):
    return str(a)
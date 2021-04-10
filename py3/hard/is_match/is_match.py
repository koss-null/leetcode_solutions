class Solution(object):
    def fit(self, s, re_piece, offset, is_next_star):
        for i, c in enumerate(re_piece):
            if not (
                c == "." or
                s[i + offset] == "." or
                c == s[i + offset] or
                (i == len(re_piece) - 1 and is_next_star)
            ):
                return False
        return True

    def check_match(self, s, rg, rg_i, offset=0):
        if rg_i == len(rg):
            return len(s) == offset
        while offset < len(s):
            if self.fit(s, rg[rg_i][0], offset, rg_i + 1 < len(rg)):
                offset += max(len(rg[rg_i][0]), 1)
                return self.check_match(s, rg, rg_i+1, offset)
            elif offset + 1 < len(s) and s[offset+1] == rg[rg_i][1]:
                offset += 1
            else:
                return False
        if offset == len(s):
            return False

    def isMatch(self, s, p):
        rg = []
        p_sp = p.split("*")
        for i, r in enumerate(p_sp):
            rg.append([r, p_sp[i-1][len(p_sp[i-1])-1] if i else "-"])

        return self.check_match(s, rg, 0)


def main(a, b):
    return Solution().isMatch(a, b)


def get_input(inp):
    return inp.split("\n")


def format_output(a):
    return str(a)

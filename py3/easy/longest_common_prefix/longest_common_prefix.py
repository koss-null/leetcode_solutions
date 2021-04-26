class Solution:
    def longestCommonPrefix(self, strs):
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            if any(filter(lambda s: s[i] != strs[0][i], strs)):
                return strs[0][:i]
        return strs[0][:min_len]


def main(*strs):
    return Solution().longestCommonPrefix(strs)


def get_input(inp):
    return inp.split()


def format_output(a):
    return a
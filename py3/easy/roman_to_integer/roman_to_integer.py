class Solution(object):
    def romanToInt(self, s):
        table = {"-": 100500, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        prev = "-"
        cache = 0
        for c in s:
            if c == prev:
                cache += table[c]
            elif table[c] < table[prev]:
                num += cache
                cache = table[c]
                prev = c
            else:
                num -= cache
                cache = table[c]
                prev = c
        return num + cache


def main():
    a = input()
    print(Solution().romanToInt(a))


if __name__ == "__main__":
    main()
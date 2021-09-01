import collections


class Solution:
    def __init__(self):
        self.triples = list()

    def count(self, nums):
        ns = collections.defaultdict(list)     # num to the list of it's indexes
        for place, n in enumerate(nums):
            ns[n].append(place)
        return ns

    def threeSum(self, nums):
        ns = self.count(nums)
        used = set()
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums[i1 + 1:]):
                if (
                    -(num1 + num2) in ns and
                    # no duplicated
                    (num1, num2, -(num1 + num2)) not in used and (
                        len(ns[-(num1 + num2)]) > 2 or
                        (
                            # checking not the same numbers
                            ns[-(num1 + num2)] != [i1, i2 + i1 + 1] and
                            ns[-(num1 + num2)] != [i2 + i1 + 1, i1] and
                            ns[-(num1 + num2)] != [i1] and
                            ns[-(num1 + num2)] != [i2 + i1 + 1]
                        )
                    )
                ):
                    self.triples.append([num1, num2, -(num1 + num2)])
                    tn = -(num1 + num2)
                    used.add((num1, num2, tn))
                    used.add((num2, num1, tn))
                    used.add((num1, tn, num2))
                    used.add((num2, tn, num1))
                    used.add((tn, num1, num2))
                    used.add((tn, num2, num1))
        return self.triples



def main(nums):
    return Solution().threeSum(ns)

def get_input(inp):
    return [int(x) for x in nums.split()]

def format_output(triples):
    pass

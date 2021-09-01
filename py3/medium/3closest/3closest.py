class Solution:
    def __init__(self):
        pass

    def findClosest(self, target, nums):
        lf, rg = 0, len(nums) - 1
        while lf < rg:
            md = lf + (rg - lf) / 2
            if abs(nums[md] - target) < abs(nums[lf] - target):
                lf = md + 1
            else:
                rg = md - 1

        if abs(nums[lf] - target) > abs(nums[rg] - target):
            return nums[rg]
        return nums[lf]

    def threeSumClosest(self, nums, target):
        closest, closest_sum = list(), 100 * 1000
        nums = sorted(nums)
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums[i1+1:]):
                desired = target - num1 - num2
                closest_third = self.findClosest(desired, nums[i1 + i2 + 1:])
                if abs(closest_third + num1 + num2 - target) < closest_sum:
                    closest_sum = abs(closest_third + num1 + num2 - target)
                    closest_third = [num1, num2, closest]
        return closest_sum

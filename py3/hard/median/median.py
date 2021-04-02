class Solution:
    def bin_search(self, arr, num, fits=lambda a, b: a == b, le=lambda a, b: a <= b):
        """
        returns tuple: the leftmost place of num in arr and the amount of items same an num
        """
        lf, rg = 0, len(arr) - 1
        md = (lf + rg) // 2
        while lf <= rg and not fits(arr[md], num):
            if le(arr[md], num):
                lf = md + 1
            else:
                rg = md - 1
            md = (lf + rg) // 2

        if arr and fits(arr[md], num):
            # searching the biggest possible step to each side and do it as many times as possible
            left_step, right_step = 1 << 20, 1 << 20
            lf_offset, rg_offset = 0, 0
            while left_step and right_step:
                if md - left_step - lf_offset < 0 or not fits(arr[md - left_step - lf_offset], num):
                    left_step >>= 1
                else:
                    lf_offset += left_step

                if md + right_step + rg_offset >= len(arr) or not fits(arr[md + right_step + rg_offset], num):
                    right_step >>= 1
                else:
                    rg_offset += right_step
            return [md - lf_offset, rg_offset + lf_offset, True]
        return [lf, 0, False]

    def place(self, nums1, nums2, num):
        """returns the leftmost and the rightmost place of the element from nums1 in merged list"""
        place1, place2 = self.bin_search(nums1, num), self.bin_search(nums2, num)
        return [place1[0] + place2[0], place1[1] + int(place1[2]) + place2[1] + int(place2[2])]

    class Shared:
        def __init__(self, nums, other_nums):
            self.p = None
            self.nums = nums
            self.other_nums = other_nums

        def fits(self, a, b):
            self.p = Solution().place(self.nums, self.other_nums, a)
            return self.p[0] <= b < self.p[0] + self.p[1]

        def le(self, _, b):
            return self.p[0] < b

    def find_place(self, nums, other_nums, desired_place):
        s = self.Shared(nums, other_nums)
        p = self.bin_search(
            nums,
            desired_place,
            fits=s.fits,
            le=s.le
        )

        if p[2]:
            return p
        return False

    def findMedianSortedArrays(self, nums1, nums2, desired_place=None, need_two=None):
        if desired_place is None:
            desired_place = int((len(nums1) + len(nums2)) / 2.0 + 0.5) - 1
        if need_two is None:
            need_two = (len(nums1) + len(nums2)) % 2 == 0

        p = self.find_place(nums1, nums2, desired_place)
        if p:
            second = nums1[p[0]]
            if need_two:
                second = self.findMedianSortedArrays(nums1, nums2, desired_place=desired_place+1, need_two=False)
            return (nums1[p[0]] + second) / 2.

        p = self.find_place(nums2, nums1, desired_place)
        if p:
            second = nums2[p[0]]
            if need_two:
                second = self.findMedianSortedArrays(nums1, nums2, desired_place=desired_place+1, need_two=False)
            return (nums2[p[0]] + second) / 2.

        print("Something went wrong")
        return -1


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(Solution().findMedianSortedArrays(a, b))


if __name__ == "__main__":
    main()

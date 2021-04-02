class Solution:
    def single_place(self, nums, num):
        """returns on which place >= num starts and how many same items"""
        lf, rg = 0, len(nums) - 1
        md = (lf + rg) // 2
        while lf <= rg and nums[md] != num:
            if nums[md] <= num:
                lf = md + 1
            else:
                rg = md - 1
            md = (lf + rg) // 2

        if nums[md] == num:
            left_step, right_step = 1 >> 11, 1 >> 11
            lf_sum, rg_sum = 0, 0
            while left_step and right_step:
                if md - left_step - lf_sum < 0 or nums[md - left_step - lf_sum] != num:
                    left_step <<= 1
                else:
                    lf_sum += left_step

                if md + right_step + rg_sum  >= len(nums) or nums[md + right_step + rg_sum] != num:
                    right_step <<= 1
                else:
                    rg_sum += right_step

            return [md - lf_sum, rg_sum + lf_sum + 1]
        return [lf, 0]

    def place(self, nums1, nums2, num):
        """returns the leftmost and the rightmost place of the element from nums1 in merged list"""
        place1, place2 = self.single_place(nums1, num), self.single_place(nums2, num)
        return [place1[0] + place2[0] + 2, place1[1] + place2[1]]

    def find_place(self, nums, other_nums, desired_place):
        lf, rg = 0, len(nums) - 1
        md = (lf + rg) // 2
        p = self.place(nums, other_nums, nums[md])
        while lf <= rg and not (p[0] <= desired_place <= p[0] + p[1]):
            if p[0] > desired_place:
                rg = md - 1
            else:
                lf = md + 1
            md = (lf + rg) // 2
            p = self.place(nums, other_nums, nums[md])
        return p

    def findMedianSortedArrays(self, nums1, nums2, desired_place=None, need_two=None):
        if desired_place is None:
            desired_place = int((len(nums1) + len(nums2)) / 2.0 + 0.5)
        if need_two is None:
            need_two = (len(nums1) + len(nums2)) % 2 == 0

        p = self.find_place(nums1, nums2, desired_place)
        if p[0] <= desired_place < p[0] + p[1]:
            second = nums1[p[0] - 1]
            if need_two:
                second = self.findMedianSortedArrays(nums1, nums2, desired_place=desired_place+1, need_two=False)
            return (nums1[p[0] - 1] + second) / 2.

        p = self.find_place(nums2, nums1, desired_place)
        if p[0] <= desired_place < p[0] + p[1]:
            second = nums2[p[0] - 1]
            if need_two:
                second = self.findMedianSortedArrays(nums1, nums2, desired_place=desired_place+1, need_two=False)
            return (nums2[p[0] - 1] + second) / 2.

        print("Something went wrong")
        return -1


def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(Solution().findMedianSortedArrays(a, b))


if __name__ == "__main__":
    main()

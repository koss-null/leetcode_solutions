class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        top_i, bot_i = 0, 0
        res = list()
        while top_i < m and bot_i < len(nums2):
            if nums1[top_i] < nums2[bot_i]:
                res.append(nums1[top_i])
                top_i += 1
            else:
                res.append(nums2[bot_i])
                bot_i += 1

        while top_i < m:
            res.append(nums1[top_i])
            top_i += 1

        while bot_i < len(nums2):
            res.append(nums2[bot_i])
            bot_i += 1
        
        for i, r in enumerate(res):
            nums1[i] = r
        
        return nums1

        
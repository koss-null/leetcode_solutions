# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object): 
    def add(self, head, lf, rg, nums):
        if lf > rg:
            return
        md = (lf + rg) // 2
        if md >= len(nums):
            return
        head.val = nums[md]

        if lf <= md - 1 and (md - 1 + lf) // 2 < len(nums):
            head.left = TreeNode()
            self.add(head.left, lf, md - 1, nums)
        if md + 1 <= rg and (md + 1 + rg) // 2 < len(nums):
            head.right = TreeNode()
            self.add(head.right, md + 1, rg, nums)


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        head = TreeNode()
        self.add(head, 0, len(nums), nums)
        return head
               
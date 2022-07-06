class Solution(object):
    def check_sum(self, node, pre_sum):
        cur_sum = pre_sum + node.val
        if node.left is None and node.right is None:
            return cur_sum == self.targetSum
        left = self.check_sum(node.left, cur_sum) if node.left else False
        if left:
            return True
        right = self.check_sum(node.right, cur_sum) if node.right else False
        if right:
            return True
        return False
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        self.targetSum = targetSum
        return self.check_sum(root, 0)
        
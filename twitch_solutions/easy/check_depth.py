 class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.max_depth = 1 << 31

    def serve(self, node, to_serve): 
        if node[0].left is None and node[0].right is None:
            if self.max_depth > node[1]:
                self.max_depth = node[1]
            return

        if node[0].left is not None:
            to_serve.append(node[0].left, node[1] + 1)
        if node[0].right is not None:
            to_serve.append(node[0].right, node[1] + 1)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        to_serve = list()
        to_serve.append((root, 1))
        while len(to_serve):
            self.serve(to_serve[0], to_serve)
            to_serve = to_serve[1:]
        return self.max_depth
        
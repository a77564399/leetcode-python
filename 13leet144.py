# Python TR
# Time：2021/8/17 10:26 上午
# coding = utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorder(root, res)

    def preorder(root, res):
        res.append(root.val)
        root.preorder(root.left,res)
        root.preorder(root.right,res)

    if __name__ == '__main__':
        root = [1, None, 2, 3]
        preorderTraversal(object,root)

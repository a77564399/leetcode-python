# Python TR
# Time：2021/8/17 1:29 下午
# coding = utf-8

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return list()

        stack = list()
        res = list()
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not (root.right) or root.right==prev:
                # print(root.right.val)
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res


    if __name__ == '__main__':
        rightTree = TreeNode(2)
        rightTree.left = TreeNode(3)
        Tree = TreeNode(1)
        Tree.right = rightTree
        print(postorderTraversal(object,Tree))
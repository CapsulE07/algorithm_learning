class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res:List[int]=[]
        if not root:
            return []
        if root.left:
            self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res:List[int]=[]
        stack:List[int]=[]
        # stack=[]
        while root and stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root = stack.pop(-1)
                res.append(root.val)
                root = root.right
        return res
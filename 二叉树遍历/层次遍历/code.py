class Solution():

    def levelOrderTraversal(TreeNode root)：
        res:List[int] = []
        queue:List[int] = []

        if not root:
            return res 
        queue.append(root)
        while queue:
            root = queue.pop(0)
            res.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        
        return res
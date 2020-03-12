class solution():

    def preorderTraversal(TreeNode root){
        stack:List[int]=[]
        res:List[int] = []
        if not root:
            return res 
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stak.append(node.left)
        
        return res

    }
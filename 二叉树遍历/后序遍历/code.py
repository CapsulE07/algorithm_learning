class solution():

    """
    方法一：在前序遍历的基础上修改
        前序遍历的访问顺序是根，左，右。
        而后续遍历的节点访问顺序是左，右，根。
        若把前序遍历的顺序改为根 ，右，左。
        最后，将结果倒置一下，即为后序遍历的结果。
    """
    def postorderTraversal(TreeNode root){
        stack:List[int]=[]
        res:List[int] = []
        if not root:
            return res 
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            res.append(root.val)
            if node.left:
                stak.append(node.left)
            if node.right:
                stack.append(node.right)
        
    
        return res[::-1]

    }
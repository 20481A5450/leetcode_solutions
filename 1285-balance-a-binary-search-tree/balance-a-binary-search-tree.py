class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Perform inorder traversal to get sorted values
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        sorted_values = inorder_traversal(root)
        
        # Step 2: Construct balanced BST from sorted values
        def sorted_list_to_bst(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(sorted_values[mid])
            node.left = sorted_list_to_bst(start, mid - 1)
            node.right = sorted_list_to_bst(mid + 1, end)
            return node
        
        return sorted_list_to_bst(0, len(sorted_values) - 1)
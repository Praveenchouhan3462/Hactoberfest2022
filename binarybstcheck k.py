def is_bst_rec(root, min_value, max_value):
  if root == None:
    return True

  if root.data < min_value or root.data > max_value:
    return False

  return is_bst_rec(root.left, min_value, root.data) and is_bst_rec(root.right, root.data, max_value)

def is_bst(root):
  return is_bst_rec(root, -sys.maxint - 1, sys.maxint)


root = create_random_BST(15)
root2 = create_random_BST(15)
root2.data = 100
print("\nInOrder Traversal")
display_inorder(root)
print("\nIs BST\n\n")
print("\nInOrder Traversal")
display_inorder(root2)
print("\nIs not BST\n\n")

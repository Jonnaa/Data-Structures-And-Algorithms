class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

# Notes to help aid the creation of insert method
# create new_node
# if root == None then root = new_node
# temp = self.root
# while loop (while true)
#   if new_node == temp reutnr False
#   if < go left, else its greater than and go right
#   if None insert new_node else move to next() (this is for both if and else)
class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self,value):
    new_node = Node(value)
    if self.root == None:
      self.root = new_node
      return True
    temp = self.root
    while True:
      if new_node.value == temp.value:
        return False
      if new_node.value < temp.value:
        if not temp.left:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if not temp.right:
          temp.right = new_node
          return True
        temp = temp.right

# Instantiate a tree using the binary search tree class
#   Note: No arguments passed since binary search tree constructor sets root to None
my_tree = BinarySearchTree()
# Insert values as needed
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

# Since no print method yet, we can print root and root left and right to check
#   that our 3 values have been inserted properly
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
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
    temp = self.root
    while(True):
      # Case 1: temp is equal to new_node, so exit
      #   this would come about if trying to insert a value that already exist
      if new_node == temp:
        return False
      # check if new_node is less than or greater than temp
      #   this would determine if we go left or right
      #   once we go left or right, we check if temp.left or temp.right
      #   is empty and we can set it to new_node
      #   else, we update temp to temp.left or temp.right to keep going down the tree
      if new_node.value < temp.value:
        if temp.left == None:
          temp.left = new_node
          return False
        # This is the else, but no need to write it
        #   since it will only run if temp.left node exists
        temp = temp.left
      else:
        if temp.right == None:
          temp.right = new_node
          return False
        # This is the else, but no need to write it
        #   since it will only run if temp.right node exists
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
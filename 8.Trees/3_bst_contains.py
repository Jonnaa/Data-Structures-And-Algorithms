##############################
# Binary Search Tree
#   Contains method
##############################

class Node:
  def __init__(self,value):
    self.value = value
    self.right = None
    self.left = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self,value):
    new_node = Node(value)
    if self.root == None:
      self.root = new_node
    temp = self.root
    while(True):
      if new_node.value == temp.value:
        return False
      if new_node.value<temp.value:
        if temp.left == None:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if temp.right ==None:
          temp.right = new_node
          return True
        temp=temp.right
  
# Steps for contains method
#   Note: make sure to compare value we are searching to node.value

# 1. Like other data structure methods, first check if empty
#   we would do this by checking if root == None, then return False
# 2. then set a var that we can use to traverse the tree
#   common name is temp
# 3. create a while loop that continues as long as temp is not None
#   if temp is None, then value does not exist in the tree
#   
#   Inside while loop
#   3.1 if value is less than temp, go left (temp=temp.left)
#   3.2 elif value is greater than temp, go right (temp=temp.right)
#   3.3 else value is equal to temp.value, return True since bst contains the value
# 4. return False

  def contains(self,value):
    if self.root == None:
      return False
    temp = self.root
    while(temp is not None):
      if value < temp.value:
        temp = temp.left
      elif value > temp.value:
        temp = temp.right
      else:
        return True
    return False 
  
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27)) #True
print(my_tree.contains(17)) #False
print(my_tree.contains(82)) #True
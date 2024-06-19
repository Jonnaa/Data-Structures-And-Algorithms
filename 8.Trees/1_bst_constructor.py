# Binary Search Tree Constructor

# First thing is to build Node class
class Node:
  #constructor
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

# Now Binary Search Tree class can be built
class BinarySearchTree:
  # constructor
  def __init__(self,value):
    # pass value to Node class to create a new node first
    new_node = Node(value)
    # Have to create root variable (head in linked list)
    #   Every other node will have something pointing to it except root, which
    #   is why we have to specify root node
    self.root = new_node
    # We will not be keeping track of length in a tree

    # This is a working binary search tree constructor, but it can be noted
    # that the constructor can also have the root point to None and then
    # later add the root and other nodes with an insert method

    # The class and constructor for such an approach would be:  
    # class BinarySearchTree:
    #   def __init__(self): Note we have removed the value parameter
    #     self.root = None
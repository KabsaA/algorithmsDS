class Node:
  def __init__(self,value,next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value
  
class LinkedList:
  def __init__(self,head_node):
    self.head_node = head_node

  def printLinkedList(self):
    a = self.head_node
    while a:
      print(a.data)
      a = a.next_node
    

from data_structures.binary_tree import BinaryTree
from code_challenges.tree_breadth_first import breadth_first



def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def fizz_buzz_tree(root):
    if not root:
        return None
    new_root = Node(root.value)
    if new_root.value % 3 == 0 and new_root.value % 5 == 0:
        new_root.value = "FizzBuzz"
    elif new_root.value % 3 == 0:
        new_root.value = "Fizz"
    elif new_root.value % 5 == 0:
        new_root.value = "Buzz"
    for child in root.children:
        new_child = fizz_buzz_tree(child)
        new_root.children.append(new_child)
    return new_root

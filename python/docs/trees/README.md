## Trees
A Binary tree is represented by a pointer to the topmost node or root of the tree. If the tree is empty, then the value of the root is None. Each Node in the tree has a value, left, and right value that help when traversing the tree.

## Challenge
Node

- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree

- Create a Binary Tree class
- Define a method for each of the depth first traversals:
- pre order
- in order
- post order
- Each depth first traversal method should return an array of values, ordered appropriately.

Binary Search Tree

- Create a Binary Search Tree class
- This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
- Add
- Arguments: value
- Return: nothing
- Adds a new node with that value in the correct location in the binary search tree.
- Contains
- Argument: value
- Returns: boolean indicating whether or not the value is in the tree at least once.
## Approach

## Binary Tree
The pre_order appends the root.value to the nodes list BEFORE invoking itself with the left and right values. Returns a list in pre order.

The in_order appends the root.value to the nodes list AFTER invoking itself with the left, but BEFORE invoking itself with the right values. Returns a list in in order.

The post_order appends the root.value to the nodes list AFTER invoking itself with the left and right values. Returns a list in post order.

## Binary Search Tree

In the add method takes in an input, if the tree is empty, the Node of the input  becomes the root. If not, it starts at the root and compares the value of the input to current Node's value. If smaller, then it makes the current Node the left Node. If larger, then it makes the current Node the right Node. This continues until the left/right Node is None and then adds the input value as a Node in that location.
The contains method takes in an input value. Starting at the root, it sees if the input value equals the value of the current Node. If not, if it's smaller, the current Node becomes the left Node. if it's larger, the current Node becomes the right Node. This continues until the input value equals the current Node's value and returns True or the value of the current Node is None and the method returns False.
Efficiency

## Time

The Big O time complexity for inserting a new node is O(n). Searching for a specific node will also be O(n). Because of the lack of organizational structure in a Binary Tree, the worst case for most operations will involve traversing the entire tree. If we assume that a tree has n nodes, then in the worst case we will have to look at n items, hence the O(n) complexity.

## Space

The Big O space complexity for a node insertion using breadth first insertion will be O(w), where w is the largest width of the tree.
The Big O space complexity of a BST search would be O(1). During a search, we are not allocating any additional space.
Source: https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html

## API
Binary Tree

pre_order - starts at the top of the tree and works left, then right returning values in pre-order.

in_order - starts at the right-most leaf, works up to the parent, then the left leaf returning values in in-order.

post_order - starts at the bottom of the tree and works right at the current level, then up one level and works left to right, until it finally reaches the root returning values in post-order.

Binary Search Tree

add - takes in a value adds a new node with that value in the correct location in the binary search tree.
contains - takes in a value and returns a boolean indicating whether the value is in the tree at least once.

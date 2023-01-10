# Challenge Summary
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process
![Tree max White board](tree_max.png)

## Approach & Efficiency
determin if the binary tree is empty

if the tree is empty return none because no value to return

if it has values use the post order method to create a list of the values
use the max method to find the mx value and return it

Time is o(n) post order at max takes the ammount of nodes to traverse

space is O(n) List will grow according to the amount of nodes it needs to add to the list 
## Solution


```python
   def find_maximum_value(self):
        if self.root is None:
            return None
        return max(self.post_order())
```

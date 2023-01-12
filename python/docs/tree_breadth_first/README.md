# Challenge Summary
Write a function called breadth first
Arguments: tree
Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process
![Tree max White board](breadth_first.png)

## Approach & Efficiency

determin if the tree is empty

if the tree is empty return none because no value to return

if it has values use the Breadth first order to add the root node to a queue pop the value off the queue add that nodes children into the results list
in left right order, this completes first loop, do loop again with each assending node as the queues next value appending each found node.value to the results list

return results

## Big O
Time is o(n) post order at max takes the ammount of nodes to traverse

space is O(n) List will grow according to the amount of nodes it needs to add to the list 
## Solution


[Breadth First Code](../../code_challenges/tree_breadth_first.py)

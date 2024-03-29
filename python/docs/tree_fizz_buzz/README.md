# Challenge Summary
* Write a function called fizz buzz tree
* Arguments: k-ary tree
* Return: new k-ary tree
* Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

  - If the value is divisible by 3, replace the value with “Fizz”
  - If the value is divisible by 5, replace the value with “Buzz”
  - If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
  - If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process
![Tree max White board](breadth_first.png)

## Approach & Efficiency

Created a function that takes in a k-ary tree as an argument, and creates a copy of that tree using the clone() method from the provided KaryTree class.

Within that function I used a helper function to take care of changing the values of the nodes depending on their divisibility by 3 and/or 5. The helper function calls itself recursively with each of the argument node's children.
Outside the helper function, the helper function is called on the cloned tree's root node.
The main function returns the cloned and fizz-buzzed list
## Big O

Time: O(n) - Each node needs to be traversed to check for divisibility by 3 and/or 5.

Space: O(n) - Each node from the original tree is copied, so each node occupies memory space so it is determined upon imput and correlates with that


## Solution

[k-ary tree code](../../code_challenges/tree_fizz_buzz.py)

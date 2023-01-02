# Stacks and Queues
- Stack: LinkedList that functions like a stack, only knows its head value and can return its head value, remove from head or add to head
- Queue: LinkedLIst that functions like a queue, only knows its head and tail value, can return its head value, remove from head and add to tail, removing returns the value of node removed

## Challenge
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Approach & Efficiency
These structures function O(1) for time and O(n) for space
They are O(1) for time because they only work with positions like head and tail in the list that are known without having to traverse

## API
Stack Methods:
  - push
    - adds to head of list
  - pop
    - removes from head and returns value of the node that was removed
  - peek
    - returns value of the head
  - is_empty
    - returns boolean if head is not None

Queue Methods:
  - enqueue
    - adds to tail of the list
  - dequeue
    - removes from head of the list and returns the value the node
  - peek
    - returns the head value
  - is_empty
    - returns boolean if head is not None


## Code and Tests
[](...)

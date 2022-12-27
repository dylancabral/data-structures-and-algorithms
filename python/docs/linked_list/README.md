# Linked List

## Challenge
<!-- Description of the challenge -->
Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
insert
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
includes
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
to string
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
Structure and Testing

Write tests to prove the following functionality:

1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
made a Node class to create new nodes.

made a LinkedList class to create a new linked list.

made an insert method to add a new node to the beginning of the list.

made an includes method to check if a value is in any of the nodes in the list.

 "to string" method to return all the values in the linked list as a string.

I used while loops to traverse through the list(s) for the includes & to string methods

## API
HUH?


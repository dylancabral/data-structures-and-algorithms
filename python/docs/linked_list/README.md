# Linked List

Linked list are important because a lot of what python is used for is data storage and interpreting and this allows us to create a vast string of connected files without storing them all in the same place Challenge

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

insert takes in a value sets self.head equal to Node(value, self.head). So the head becomes a new Node which has a value of the input and next being the current value of the head.

includes tries to find a input value in the linked list. It takes in a value and sets current equal to self.head and runs a while loop until current is equal to None. If the current.value equals the input value, then the method returns True. If not, the loop sets current equal to current.next and continues the loop. If the current value becomes None, then the linked list does not contain the input value and the method returns False.

__str__ returns the linked list as a string. It sets current equal to self.head, creates an emtpy string variable, and runs a while loop until current is equal to None. While current does not equal None, then the string is appended with { } -> that contains the current.value inside the curly brackets. Once current equals None, string is appended with NULL. The string variable now contains all values of the linked list and ends with "NULL".

## link to code

[linked list code](../../data_structures/linked_list.py)

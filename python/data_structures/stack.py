from python.data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval

class Stack:
    """
    Linked List that functions strictly like a Stack. Knows its top only. Pop returns the value of the popped item.
    """

    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        # if self.top is None:
        #     raise InvalidOperationError("Method not allowed on empty collection")
        try:
            value = self.head.value
            self.head = self.head.next
            return value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.head.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.head is None

from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value=None, nextval=None):
        self.value = value
        self.next = nextval

class Queue:
    """
    Linked list that functions as a Queue. Knows head and tail, enqueue adds to end and dequeue removes from head
    """

    def __init__(self):
        self.front = None
        self.tail = None

    def enqueue(self, value):
        if self.tail:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            return
        self.tail = self.front= Node(value)

    def dequeue(self):
        try:
            dequeued = self.front
            self.front = self.front.next
            return dequeued.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        try:
            return self.front.value
        except Exception as e:
            raise InvalidOperationError("Method not allowed on empty collection")

    def is_empty(self):
        return self.front is None

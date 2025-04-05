"""Implement Stack using Queues"""

class Node:
    """class for node"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    """class for queue"""
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """if it is empty"""
        return self.head is None

    def add(self, item):
        """add item at the end"""
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        """pop item from the beginning"""
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        """peek item from the beginning"""
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


class MyStack(object):
    """class for MyStack"""
    def __init__(self):
        self.queue_ = Queue()

    def push(self, x):
        """
        push item at the end
        :type x: int
        :rtype: None
        """
        self.queue_.add(x)
        for _ in range(len(self.queue_) - 1):
            self.queue_.add(self.queue_.pop().item)


    def pop(self):
        """
        pop item from the end
        :rtype: int
        """
        if self.queue_.is_empty():
            raise ValueError("Stack is empty.")
        return self.queue_.pop().item


    def top(self):
        """
        :rtype: int
        """
        if not self.queue_.is_empty():
            return self.queue_.peek
        raise ValueError('Stack is empty')


    def empty(self):
        """if it is empty"""
        return self.queue_.is_empty()

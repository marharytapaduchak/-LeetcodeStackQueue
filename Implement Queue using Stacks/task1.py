"""Implement Queue using Stacks"""
class Node:
    """class for node"""
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    """class for Stack"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """if it is empty"""
        return self.head is None

    def push(self, item):
        """pust item at the end"""
        self.head = Node(item, self.head)

    def pop(self):
        """pop item from the end"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        """peek item from the end"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s = str(current.item) + ' ' +s
            current = current.next
        return 'bottom -> '+ s+'<- top'


class MyQueue(object):
    """class for MyQueue"""
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x):
        """push item at the end"""
        self.stack_in.push(x)

    def pop(self):
        """pop item from the beginning"""
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """peek item from the beginning"""
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek

    def empty(self):
        """if it is empty"""
        return self.stack_in.is_empty() and self.stack_out.is_empty()

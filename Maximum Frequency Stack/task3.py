"""Maximum Frequency Stack"""
from collections import deque, defaultdict

class FreqStack(object):
    """class for FreqStack"""
    def __init__(self):
        self.stack = deque()
        self.freq = defaultdict(int)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.freq[val] += 1


    def pop(self):
        """
        :rtype: int
        """
        max_freq = max(self.freq.values())

        temp = deque()
        res = None

        while self.stack:
            val = self.stack.pop()
            if res is None and self.freq[val] == max_freq:
                res = val
                self.freq[val] -= 1
                break
            temp.appendleft(val)

        self.stack.extend(temp)
        return res

import itertools
from heapq import heappop, heappush


# From https://docs.python.org/3/library/heaself.pq.html#priority-queue-implementation-notes
# Only additions were indexing the entry_finder by using states as keys and then removing using the state keys
class PriorityQueue:
    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<self.REMOVED-task>'  # placeholder for a self.REMOVED task
        self.counter = itertools.count()  # unique sequence count

    def add_task(self, task, priority=0):
        """Add a new task or update the priority of an existing task"""
        if task.state[1:] in self.entry_finder:
            self.remove_task(task.state[1:])
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task.state[1:]] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        """Mark an existing task as self.REMOVED.  Raise KeyError if not found."""
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task.state[1:]]
                return task
        raise KeyError('pop from an empty priority queue')

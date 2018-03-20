class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
import collections
def getImportance(employees,id):
    total = 0
    dict = {}
    for i in employees:
        dict[i.id] = i
    queue = collections.deque()
    queue.append(dict.get(id))
    while queue:
        current = queue.pop()
        total += current.importance
        for i in current.subordinates:
            queue.append(dict.get(i))
    return total


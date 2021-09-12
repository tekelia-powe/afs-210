class NodeSinglePointer:
    def __init__(self, data=None):
        self.data = data    #passed to make a node
        self.next = None    #points to the next node
                            #None means it is at the end
    # This def passes data to print() when called
    def __str__(self):
        return str(self.data)   #Text leaves out self.

class SinglyLinkedList:
    def __init__(self):
        self.head = None    # Placeholder for insert point
        self.tail = None    # Placeholder for first item
        self.size = 0       # New list has no members

    def append(self, data):  # Pass data to append
        # Put the data in a new node
        node = NodeSinglePointer(data)

        if self.head:   # Already an insertion pointer
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node    # This is the first one
    
    # A function to iterate over the list items
    # and yield the data values
    def iter(self):
        current_node = self.tail    # The first one
        while current_node:
            val = current_node.data
            current_node = current_node.next
            yield val
print('Expected Output:')
languages = SinglyLinkedList()     # new instance
languages.append('PHP')
languages.append('Python')
languages.append('C#')
languages.append('C++')
languages.append('Java')
for val in languages.iter():
    print(val)
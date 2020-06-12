class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        if self.value:
         return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False



    def reverse_list(self, node, prev):
        # if no value return nothing
        if not node:
            return
        # if no next node set the head to be the input node
        if not node.get_next():
            self.head = node
            return
        # call recursively and pass in the next node
        # as the node, and the current node as the
        # previous node
        self.reverse_list(node.get_next(), node)
        # get the next node and set it to the next node
        node.get_next().set_next(node)
        # set the next node afer that to None
        node.set_next(None)


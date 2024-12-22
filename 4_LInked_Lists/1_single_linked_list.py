class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        temp_node = self.head
        output = ""
        while temp_node is not None:
            output += str(temp_node.data) + " "
            temp_node = temp_node.next
        return output


my_list = LinkedList()
my_list.append(23)
my_list.append(27)
my_list.append(20)
my_list.prepend(56)


print(my_list)



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string[:-3]


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)


    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


    def copy(self):
        copy = LinkedList()
        node = self.head
        while node:
            new_node = Node(node.value)
            copy.append(new_node)
            node = node.next
        return copy


    def previous_node(self, ref_node):
        node = self.head #if the LL only has one element, result is None
        while node and (node.next != ref_node):
            node = node.next
        return node


    def remove(self, node):
        prev_node = self.previous_node(node)
        if not prev_node:
            self.head = self.head.next
        else:
            prev_node.next = node.next


    def remove_duplicates(self):
        copy = self.copy()
        node_1 = copy.head
        while node_1:
            node_2 = node_1.next
            val = node_1.value
            while node_2:
                temp = node_2
                node_2 = node_2.next
                if temp.value == val:
                    copy.remove(temp)
            node_1 = node_1.next
        return copy


def union(llist_1, llist_2):
    # Your Solution Here
    if not llist_1.head:
        union = llist_2.copy()
        return union.remove_duplicates()

    if not llist_1.head:
        union = llist_1.copy()
        return union.remove_duplicates()

    union = llist_1.copy()
    node = union.head
    while node.next:
        node = node.next
    llist2_copy = llist_2.copy()
    node.next = llist2_copy.head
    return union.remove_duplicates()


def intersection(llist_1, llist_2):
    # Your Solution Here
    if (not llist_1.head) or (not llist_2.head):
        return LinkedList()

    intersect = LinkedList()
    node_1 = llist_1.head
    node_2 = llist_2.head
    while node_1:
        val = node_1.value
        while node_2:
            if node_2.value == val:
                intersect.append(Node(val))
                break
            node_2 = node_2.next
        node_1 = node_1.next

    return intersect.remove_duplicates()


if __name__ == '__main__':
    # Test case 1

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 4, 3]

    # element_1 = [3,2,4,35,6,65,6,4,3,21]
    # element_2 = [6,32,4,9,6,1,11,21,1]
    #
    for i in element_1:
        linked_list_1.append(i)

    print (linked_list_1.remove_duplicates())
    #
    # for i in element_2:
    #     linked_list_2.append(i)
    #
    # print (union(linked_list_1,linked_list_2)) #should be (1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65)
    # print (intersection(linked_list_1,linked_list_2)) #should be (4, 6, 21)
    #
    # # Test case 2
    #
    # linked_list_3 = LinkedList()
    # linked_list_4 = LinkedList()
    #
    # element_1 = [3,2,4,35,6,65,6,4,3,23]
    # element_2 = [1,7,8,9,11,21,1]
    #
    # for i in element_1:
    #     linked_list_3.append(i)
    #
    # for i in element_2:
    #     linked_list_4.append(i)
    #
    # print (union(linked_list_3,linked_list_4)) #should be (1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65)
    # print (intersection(linked_list_3,linked_list_4)) #should be (2)
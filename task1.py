class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        acc = []
        while current:
            acc.append(current.data)
            current = current.next
        print(acc)

    def reverse(self):
        active = self.head
        previous = None

        while active:
            next_node = active.next
            active.next = previous
            previous = active
            active = next_node
        self.head = previous

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next

            if sorted_head is None or sorted_head.data > current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next is not None and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head

    def merge_sorted_lists(self, other):
        merged_list = LinkedList()
        self_active = self.head
        other_active = other.head

        while self_active is not None and other_active is not None:
            if self_active.data < other_active.data:
                merged_list.insert_at_end(self_active.data)
                self_active = self_active.next
            else:
                merged_list.insert_at_end(other_active.data)
                other_active = other_active.next

        while self_active:
            merged_list.insert_at_end(self_active.data)
            self_active = self_active.next

        while other_active:
            merged_list.insert_at_end(other_active.data)
            other_active = other_active.next

        self.head = merged_list.head


def new_llist(delta=0):
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(10 + delta)
    llist.insert_at_beginning(5 + delta)
    llist.insert_at_beginning(15 + delta)

    # Вставляємо вузли в кінець
    llist.insert_at_end(25 + delta)
    llist.insert_at_end(20 + delta)

    return llist


llist_1 = new_llist()
print("Новий зв'язний список:")
llist_1.print_list()


print("\nPеверсування однозв'язного списку")
llist_1.reverse()
llist_1.print_list()


print("\nСортування однозв'язного списку")
llist_1.insertion_sort()
llist_1.print_list()


llist_2 = new_llist(10)

# Об'єднує два відсортовані однозв'язні списки
print("\nОб'єднує два відсортовані однозв'язні списки")
llist_2.print_list()
print("----")
llist_1.merge_sorted_lists(llist_2)
llist_1.print_list()

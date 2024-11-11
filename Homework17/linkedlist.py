class Node:
    def init(self, data=None):  # Node klasis konstruqtori
        self.data = data  # nodeshi datas shenaxva
        self.next = None  # shemdegi nodes pointer(default is None)


class LinkedList:
    def init(self):  # LinkedList klasis konstruqtori
        self.head = None  # carieli listis inicializacia

    # methodi rom append gavuketot axal nodes listis boloshi
    def append(self, data):
        new_node = Node(data)  # axali nodes sheqmna
        if self.head is None:  # tu listi carielia
            self.head = new_node  # axali node iyos dasawyisi
            return

        last_node = self.head
        while last_node.next:  # bolo nodeze misvla
            last_node = last_node.next

        last_node.next = new_node  # damateba

    # mititebul indexze nodes washlis metodi
    def remove_at(self, index):
        if index < 0 or self.head is None:  # tu index arasworia and nullia
            return

        if index == 0:  # tu 0 ia moacilebs pirvels(anu listis pirvelive nodes)
            self.head = self.head.next  # listis "heads" gadaitans shemdeg nodeze, anu [1] node chamova [0] ze.
            return

        # gadmocemul indexamde misvla
        current_node = self.head
        current_position = 0

        while current_node.next and current_position < index - 1:
            current_node = current_node.next  # shemdeg nodeze gadasvla
            current_position += 1

        if current_node.next:  # tu eseti node arsebobs
            current_node.next = current_node.next.next  # wavshalot target node

    def add_at_index(self, index, data):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        current_node = self.head
        current_position = 0
        while current_node and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
            return True
        return False

    def remove_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next
            return True
        return False

    # linkedin listis dabechdva
    def display(self):
        current_node = self.head  # dasawyisidan
        while current_node:  # titoeuli node
            print(current_node.data, end=' -> ')  # print
            current_node = current_node.next  # shemdeg nodeze gadasvla

        print()  # Print a new line


# shevqmnat linkedlist instansi
linked_list = LinkedList()

# Listshi nodebis chamatebis demonstracia
linked_list.append(50)
linked_list.append(15)
linked_list.append(20)
linked_list.append(11)
linked_list.append(5)
linked_list.append(25)

# print
linked_list.display()

# 2 indexze nodes washla
linked_list.remove_at(2)
linked_list.display()

# isev 2 indexze remove (moacilebs '11')
linked_list.remove_at(2)
linked_list.display()  # Output: 50 -> 15 -> 5 -> 25 ->

# 0 indexze remove (moacilebs head '50')
linked_list.remove_at(0)
linked_list.display()

# 2 indexze mocileba (removing '25')
linked_list.remove_at(2)
linked_list.display()

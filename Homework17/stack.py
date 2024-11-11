# node class sheqmna
class Node:
    def init(self, data=None):  # node konstruqtori
        self.data = data
        self.next = None


# stack class sheqmna
class Stack:
    def init(self):  # stack class konstruqtori
        self.top_node = None  # stakis top_node rogorc None, anu carieli staki
        self.length = 0  # Initialize stack size to 0

    # metodi rom shevamowmot aris tu ara staki carieli
    def empty(self):
        return self.length == 0

    # abrunebs stackshi arsebuli elementebis raodenobas
    def size(self):
        return self.length

    # axali datas damateba stakshi
    def push(self, data):
        new_node = Node(data)  # nodes vqmnit gadmocemuli datati
        new_node.next = self.top_node  # axlandeli top node gadaqvaqvs nextze
        self.top_node = new_node  # top_nodes vanichebt axal nodes
        self.length += 1  # stack sizes +1

    def remove_value(self, value):
        temp_stack = Stack()
        removed = False

        while not self.empty():
            top_value = self.pop()
            if top_value == value and not removed:
                removed = True
                continue
            temp_stack.push(top_value)

        while not temp_stack.empty():
            self.push(temp_stack.pop())

        return removed

    def add_at_index(self, index, data):
        if index < 0 or index > self.length:
            return False

        temp_stack = Stack()
        for _ in range(index):
            temp_stack.push(self.pop())

        self.push(data)

        while not temp_stack.empty():
            self.push(temp_stack.pop())

        return True

    # remove metodi stakis top_nodestvis
    def pop(self):
        if not self.empty():  # vamowmebt carielia tu ara staki
            popped_item = self.top_node.data  # top nodes data
            self.top_node = self.top_node.next  # top node gadavitanot next nodeze
            self.length -= 1  # stack size -1
            return popped_item  # davabrunot "popped_item"
        else:  # tu staki carielia indexError
            raise IndexError("Stack is empty")


# axali stakis instance
stack = Stack()

# vamowmebt staki aris tu ara carieli da shemdeg vprintavt elementebis raodenobas
print(stack.empty())
print(stack.length)

# vamatebt datas
stack.push(200)
stack.push(50)
stack.push(75)
stack.push(25)
stack.push(30)

# vamowmebt staki aris tu ara carieli da shemdeg vprintavt elementebis raodenobas itemebis damatebis shemdgom
print(stack.empty())
print(stack.length)

# vaketebt pops da shemdeg isev vamowmebt statuss
print(stack.pop())  # Output: 30 (top item is removed)
print(stack.empty())
print(stack.length)

print(stack.pop())  # Output: 25 (top item is removed)
print(stack.length)  # Output: 3 (three elements left)

print(stack.pop())  # Output: 75 (top item is removed)
print(stack.length)  # Output: 2 (two elements left)

print(stack.pop())  # Output: 50 (top item is removed)
print(stack.length)  # Output: 1 (one element left)

print(stack.pop())  # Output: 200 (last item is removed)
print(stack.empty())  # Output: True (stack is now empty)
print(stack.length)  # Output: 0 (no elements in the stack)

# cariel stakze pop-is mcdeloba aq
print(stack.pop())  # IndexError: "Stack is empty"

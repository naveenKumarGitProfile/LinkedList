class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def transversal(self):
        if self.head is None:
            print("The linked List is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end = " ")
                a = a.next

    def insertAtBeginning(self,data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insertAtEnd(self,data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    def insertAtSpecific(self,position,data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1,position-1):
            a = a.next
        nib.next = a.next
        a.next = nib

    def deletionAtBeginning(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None

    def deletionAtEnd(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def deletionAtParticularNode(self,position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1,position-1):
            a = a.next
            prev  = prev.next
        prev.next = a.next
        a.next = None



llist = LinkedList()
llist.head = Node(10)
second = Node(15)
third = Node(20)
fourth = Node(25)

llist.head.next = second
second.next = third
third.next = fourth
llist.transversal()
llist.insertAtBeginning(5)
llist.transversal()
llist.insertAtEnd(30)
llist.transversal()
llist.insertAtSpecific(3,12)
llist.transversal()
llist.deletionAtBeginning()
llist.transversal()
llist.deletionAtEnd()
llist.transversal()
llist.deletionAtParticularNode(4)
llist.transversal()
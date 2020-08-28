class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size=0

    def insertEnd(self,data):

        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode
    
    
        

    def traverseList(self) :
        actualNode = self.head
        while actualNode is not None:
            print("%d " % actualNode.data,end=" ")
            actualNode = actualNode.nextNode


def merge(a,b):    
    if a is None:
        return b
    elif b is None:
        return a
    if a.nextNode is not None:
        temp=a.nextNode
    else:
        a.nextNode=b
        return a
    if b.nextNode is not None:
        temp1=b.nextNode
    else:
        a.nextNode=b
        return a
    start=a
    while(a is not None and b is not None):
            a.nextNode=b
            if b ==  temp1:
                break
            if a == temp:
                break
            b.nextNode=temp
            a=temp
            b=temp1
            if temp.nextNode is not None:
                temp=temp.nextNode
            else:
                pass
            if temp1.nextNode is not None:
                temp1=temp1.nextNode
            else:
                pass 
            
    print(a.data)
    print(temp.data)
    print(b.data)
    print(temp1.data)
    if a != temp and b == temp1 :
        while temp is not None:
            b.nextNode=temp
            b=temp
            temp=temp.nextNode
    elif a == temp and b != temp1:
        while temp1 is not None:
            b.nextNode=temp1
            b=temp1
            temp1=temp1.nextNode


    return start
            


linkedlist1=LinkedList()
linkedlist2=LinkedList()


t=int(input("Enter the number of linked list "))
while(t):
    b=int(input(f"\nEnter choice for  link list {t} \n 1 to insert \n 2 to traverse \n 0 to exit: \n "))
    if b==1:
        a=int(input("Enter a number: "))
        linkedlist1.insertEnd(a)
    elif b==2:
        linkedlist1.traverseList()
    
    t=t-1


b=1
while(b):
    b=int(input("\nEnter choice\n 1 to insert \n 2 to traverse \n 0 to exit: \n "))
    if b==1:
        a=int(input("Enter a number: "))
        linkedlist2.insertEnd(a)
    elif b==2:
        linkedlist2.traverseList()




actualNode=merge(linkedlist1.head,linkedlist2.head)
while actualNode is not None:
            print("%d " % actualNode.data,end=" ")
            actualNode = actualNode.nextNode
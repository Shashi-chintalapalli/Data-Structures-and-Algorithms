class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def print(self):
        
        if self.next is None:
            print("LinkdedList is empty")
            return
        ltr=self.head
        lltr=''
        while ltr:
            if ltr.next:
                lltr+=str(ltr.data)+'-->'
            else:
                str(ltr.data)
        print(lltr)


        
             
        
        
class linkedlist:
    def __init__(self,val=val)
        self.val=val
        self.next=None
class node:
    def add_two_num(self,l1,l2):
        node=linkedlist()
        carry=0

        while l1==None or l2==None or carry==0:
            l1=l1.val if l1 else 0
            l2=l2.val if l2 else 0

            rus=l1+l2+carry
            carry=rus//10
            rus=rus%10
            node.next=linkedlist(rus) if node!=None: else node=linkedlist(rus)

            l1=l1.next
            l2=l2.next

            




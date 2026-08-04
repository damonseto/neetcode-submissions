# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        count = 0
        counter = head
        while counter:
            count += 1
            counter = counter.next
        count = (count + 1) // 2
        counter = head
        node = ListNode()
        node.next = head
        for i in range(0, count):
            counter = counter.next
            node = node.next
        start2 = counter
        node.next = None
        prev = None
        while start2:
            old = start2
            var = start2.next
            start2.next = prev
            prev = old
            start2 = var

        inc = head 
        while inc and prev:
            temp1 = inc.next
            temp2 = prev.next
            inc.next = prev
            prev.next = temp1
            inc = temp1
            prev = temp2
        

        



        
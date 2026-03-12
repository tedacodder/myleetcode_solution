# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=None
        while head:
            while stack and stack.val<head.val:
                stack=stack.next
            newnode=ListNode(head.val,stack)
            stack=newnode
            
            head=head.next
        def reverseList(head):
            prev = None
            curr = head

            while curr:
                next_node = curr.next   # store next node
                curr.next = prev        # reverse the link
                prev = curr             # move prev forward
                curr = next_node        # move curr forward

            return prev

        return reverseList(stack)
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            nextNode = slow.next
            slow.next = pre
            pre = slow
            slow = nextNode
        ## 奇数链表时，fast此时非None，  
        ## 所以slow需要前进一步
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != pre.val:
                return False
            slow=slow.next
            pre=pre.next
        return True
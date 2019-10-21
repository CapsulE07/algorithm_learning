
## Rotate List

### Tags
linked-list | two-pointers

### description
Given a linked list, rotate the list to the right by k places, where k is non-negative.

### Examples
```
Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

### code
```
"""
231/231 cases passed (40 ms)
Your runtime beats 86.28 % of python3 submissions
Your memory usage beats 6.45 % of python3 submissions (13.9 MB)
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        end = head
        count = 1
        while end and end.next:
            end = end.next
            count += 1
        
        rotateTimes = k % count
        if rotateTimes ==0:
            return head
        start = head
        count_1 = 1
        newEnd = None
        resNum = count - rotateTimes
        while count_1 <= resNum:
            newEnd = start
            start = start.next
            count_1 += 1
        end.next=head
        newEnd.next= None
        return start
        
```



```
"""
231/231 cases passed (40 ms)
Your runtime beats 86.28 % of python3 submissions
Your memory usage beats 6.45 % of python3 submissions (13.6 MB)
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        if head.next == None:
            return head
            
        pointer = head
        length = 1
        
        while pointer.next:
            pointer = pointer.next
            length += 1
        
        rotateTimes = k%length
        
        if k == 0 or rotateTimes == 0:
            return head
        
        fastPointer = head
        slowPointer = head
        
        for a in range (rotateTimes):
            fastPointer = fastPointer.next
        
        
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        
        temp = slowPointer.next
        
        slowPointer.next = None
        fastPointer.next = head
        head = temp
        
        return head
```
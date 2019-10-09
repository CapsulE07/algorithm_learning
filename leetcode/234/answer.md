# 234.回文链表  
## 描述  
请判断一个链表是否为回文链表

## 示例
```
输入: 1->2 
输出: false

输入: 1->2->2->1 
输出: true
```

## 进阶： 
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


## 解决思路  
可以设置快慢指针，当快指针走完时，慢指针刚好走到中点，同时慢指针一边前进同时反转链表方向，直至走至中点。随后用另一个指针沿着反转链表方向前进，同时慢指针继续遍历后续链表，两指针一边遍历一边对比。  
需要留意奇偶数链表对于中点的选取的边界选择。

```
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
```
##  [Leetcode] 23. Merge k Sorted lists
###  Description 
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

### Tags
linked-list | divide-and-conquer | heap
### Example 
```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

```
## 解决方案

### 分治法
思路： 借鉴 \[Leetcode\] 21. Merge k Sorted lists,两两合并即可。
```
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0 or not lists:
            return 
        return self.merge(lists,0, len(lists)-1)
    
    def merge(self, lists, l, r):
        if l < r:
            mid = (l+r) //2
            return self.mergeTwoLists(self.merge(lists,l,mid), self.merge(lists,mid+1,r))
        return lists[l]
    
    def mergeTwoLists(self, l1, l2):
        res = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur=cur.next
        cur.next=l1 or l2
        return res.next
```

### 堆排序
使用

```

```
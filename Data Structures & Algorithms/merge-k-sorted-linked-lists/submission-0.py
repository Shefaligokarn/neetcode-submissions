# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwolists(list1, list2):
            dummy = ListNode(0)
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 or list2
            return dummy.next
        while (len(lists)) >1:
            merged = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                merged.append(mergetwolists(l1,l2))
            lists = merged

        return lists[0] if lists else None
        

    




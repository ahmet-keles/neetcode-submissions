# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = head
        res = []
        while dummy:
            res.append(dummy.val)
            dummy = dummy.next
        l = 0
        r = len(res) - 1
        while l <= r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True
#Time_Complexity: O(n) 
#Space_Complexity : O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # initializing prev 
        curr = head # initializing curr to head
        
        while curr: # run until curr not equal to null
            temp = curr.next # setting temp to curr.next
            curr.next = prev # changing pointer to prev
            prev = curr # assigning curr to prev
            curr = temp # assigning temp to curr
            
        return prev # returning prev

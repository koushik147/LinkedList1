class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 # assigning count to 0
        dummy = ListNode(" ",head) # initializing dummy node
        slow = dummy # setting slow to dummy
        fast = dummy #setting fast to dummy
        
        while count<n: # run until count is less than n
            fast = fast.next 
            count += 1
            
        while fast.next!=None: # run until fast.next not equal to none
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next # redirecting the slow pointer to slow.next.next
        
        return dummy.next #returning dummy.next
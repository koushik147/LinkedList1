#Time_Complexity: O(n) 
#Space_Complexity : O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        slow = head # assigning head to slow
        fast = head # assigning head to fast
        cycle = False # assigning cycle to false initially
        
        while fast!=None and fast.next!=None: # run until fast and fast.next not equal to none
            slow = slow.next # incrementing 1 node
            fast = fast.next.next # incrementing 2 nodes
            
            if slow == fast: # if slow is equal to fast
                cycle = True # assigning cycle to true
                break
                
        if not cycle:
            return None # if not return nothing
        
        slow = head 
        while slow != fast: # run until slow not equal to fast
            slow = slow.next # incrementing 1 node
            fast = fast.next # incrementing 1 node
            
        return slow

#大概是判断链表有没有环
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

node1 , node2, node3, node4, node5= ListNode(1) ,ListNode(1) ,ListNode(3) ,ListNode(4) ,ListNode(5)
node1.next , node2.next , node3.next , node4.next , node5.next = node2 , node3 , node4 , node5 , node1
a = Solution().hasCycle(node1)
print(a)

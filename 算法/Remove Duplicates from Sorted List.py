#在排好序的链表中删除重复值
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        now = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next

            head = head.next
        return now
node1 , node2, node3, node4, node5= ListNode(1) ,ListNode(2) ,ListNode(3) ,ListNode(1) ,ListNode(5)
node1.next , node2.next , node3.next , node4.next , node5.next = node2 , node3 , node4 , node5 , None
a = Solution().deleteDuplicates(node1)
head = node1
while head:
    print(head.val)
    head = head.next
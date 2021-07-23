'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

题意：对给定的排好序的链表，删除重复的元素，只留下出现一次的元素





解题思路：创建两个链表，一个负责保存头节点，一个负责记录比较后的结果。
'''
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
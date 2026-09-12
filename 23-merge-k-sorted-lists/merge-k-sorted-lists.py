class Solution:
    def mergeKLists(self, lists):
        result = []

        for head in lists:
            while head:
                result.append(head.val)
                head = head.next

        result.sort()

        dummy = ListNode(0)
        current = dummy

        for value in result:
            current.next = ListNode(value)
            current = current.next

        return dummy.next
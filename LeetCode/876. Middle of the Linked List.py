class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        count = 0
        while head != None:
            nodeList.append(head)
            head = head.next
            count +=1
        return nodeList[count//2]
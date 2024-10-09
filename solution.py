# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1:list[int], l2:list[int]):
  
            
        number1 = 0
        number2= 0
        for digit1,digit2 in zip(l1,l2):
            number1 = number1 *10 + digit1
            number2 = number2 *10 + digit2
        total = number2+number1
        inverted = int(str(total)[::-1])
        print(inverted,total,number1,number2)
        

a = Solution()
a.addTwoNumbers([3,2,1],[2,3,1])
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

from utils.Types.singly_linked_list import ListNode, generate_list
import utils.file_rename as file_rename
from utils.printers import print_liked_list  

file_rename.rename_file("206. Reverse Linked List", __file__)

def solution(head: ListNode) -> ListNode:
    if(not head): return head

    rev_head = None
    while(head):
        temp_next = head.next
        head.next = rev_head
        rev_head = head
        head = temp_next
    
    return rev_head


# def solution_rec_main(head: ListNode) -> ListNode:
# # My attempted recursion. works but looks ugly.
#     stack = []
#     tail = None;
#     def rec(head, tail):
#         if not head.next:
#             tail = head;
#             return (head, head)

#         p, tail = rec(head.next, tail)
#         p.next = head
#         head.next = None
#         p = head
#         return p, tail

#     _, tail = rec(head, tail)
#     return tail

def solution_rec_main(head: ListNode) -> ListNode:
    # gpt's answer after asked to improve my attemt
    def rec(node: ListNode):
        # n0 => n1 => ... => nN-1 => nN => None
        # reach end of list, return nN
        # node = nN-1, node.next.next is nN.next, set nN.next to nN-1(nN-1 <=> nN)
        # set nN-1.next to None, now head is (nN => nN-1 => None)
        # now (n0 => n1 => ... => nN-2 => nN-1 => None), and head (nN => nN-1 => None)
        # return nN

        # node = nN-2, node.next.next is nN-1.next, set nN-1.next to nN-2 (nN => nN-1 <=> nN-2)
        # set nN-2.next to None, now head is (nN => nN-1 => nN-2 => None)
        # now (n0 => n1 => ... => nN-3 => nN-2 => None), and head (nN => nN-1 => => nN-2 => None)
        # return nN

        #...

        if not node or not node.next:
            return node
        
        new_head = rec(node.next)
        node.next.next = node
        node.next = None
        return new_head

    return rec(head)




head = generate_list([x for x in range(0, 6)])

print_liked_list(head)
print_liked_list(solution_rec_main(head))
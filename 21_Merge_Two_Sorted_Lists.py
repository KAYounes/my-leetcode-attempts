"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from utils.Types.singly_linked_list import ListNode, generate_list
from utils.printers import print_liked_list


def solution(list1: ListNode, list2: ListNode):
    _sorted = ListNode() # final sorted list
    _current = _sorted # tail node of sorted list

    while list1 and list2:
        if(list1.val <= list2.val):
            _current.next = list1
            list1 = list1.next

        else:
            _current.next = list2
            list2 = list2.next

        _current = _current.next


    if not list1:
        _current.next = list2
    else:
        _current.next = list1
    
    # first node was a placeholder
    return _sorted.next




list1 = generate_list([1, 2, 4])
list2 = generate_list([3, 4, 5])
print_liked_list(list1, "list1:")
print_liked_list(list2, "list2:")
print_liked_list(solution(list1, list2))
print()



list1 = generate_list([1, 2])
list2 = generate_list([3, 4, 5])
print_liked_list(list1, "list1:")
print_liked_list(list2, "list2:")
print_liked_list(solution(list1, list2))
print()



list1 = generate_list([1, 2, 4])
list2 = generate_list([3, 4])
print_liked_list(list1, "list1:")
print_liked_list(list2, "list2:")
print_liked_list(solution(list1, list2))
print()



list1 = generate_list([1])
list2 = generate_list([3, 4, 5])
print_liked_list(list1, "list1:")
print_liked_list(list2, "list2:")
print_liked_list(solution(list1, list2))
print()

list1 = generate_list([1, 3])
list2 = generate_list([3])
print_liked_list(list1, "list1:")
print_liked_list(list2, "list2:")
print_liked_list(solution(list1, list2))
print()


list1 = generate_list([])
list2 = generate_list([])
print_liked_list(list1, "list1:")
print_liked_list(list2, "list2:")
print_liked_list(solution(list1, list2))
print()
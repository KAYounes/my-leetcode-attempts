from math import log
from turtle import st
from utils.Types.singly_linked_list import ListNode, generate_list
import utils.file_rename as file_rename
from utils.printers import print_dict, print_liked_list  

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


head = generate_list([x for x in range(-10, 11)])

print_liked_list(head)
print_liked_list(solution(head))
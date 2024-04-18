class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f"ListNode(val: ${self.val}, next: ${self.next.__str__()})"
    
def generate_list(values):

    if not values or not len(values): return None
    head = ListNode(values[0])
    tail = head

    for value in values[1:]:
        tail.next = ListNode(value, None)
        tail = tail.next
    
    return head


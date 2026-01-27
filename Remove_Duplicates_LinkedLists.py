#First create another list
dummy = ListNode(0)      # new linked list (l2 equivalent)
tail = dummy             # tail pointer for new list
current = head           # traversal starts

while current :
  # if next exists and is duplicate, skip duplicates
  if current.next and current.val == current.next.val:
    current = current.next
  else:
    # unique value → add to new list
    tail.next = ListNode(current.val)
    tail = tail.next
    current = current.next
return dummy.next        # head of new linked list

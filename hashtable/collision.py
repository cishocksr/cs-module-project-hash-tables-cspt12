
# - hash function + array = hash table
#                     -array full of linked lists


# index  Chain
# 0       None
# 1       None
# 2       None
# 3       None
# 4       None
# 5       None


# put('foo', 12) # hash to 1
# put('baz', 13) # hash to 3
# put('bar', 23) # hash to 1

# get('bar') 

# How do we do a get when handling collision with linked list
# Store the key unhashed, and compare as we iterate/traverse down the linked list

# put 
#     Check if key is in linked list if so overwrite if not add new Node

# delete
#     delete('bar')
#     find the matching pair of values
#     -point the previous node of that one to the next node of the found node
#     -
    


# Linked lists
# - Single linked node.next
# - Double linked, node.next and node.prev


class SLL:
    def __init__(self):
        self.head = None
    
    def get(self, value):
        # start at the head
        node = self.head
        while node is not None:
        # check for the target value
            if node.value == target_value:
                return node
            # move to next node
                else:
                    node = node.next



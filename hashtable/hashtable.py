class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.length = 0

    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur
            else:
                cur = cur.next

        return None

    def insert_at_head(self, node):
        # first search for key in list
        found_node = self.find(node.key)
        # replace value if key already exists
        if found_node is not None:
            found_node.value = node.value
        # else add a new node to the head
        else:
            node.next = self.head
            self.head = node

    def delete(self, key):
        if self.head.key == key:
            old_head = self.head
            self.head = self.head.next

            return old_head

        else:
            cur = self.head.next
            prev = self.head

            while cur is not None:
                if cur.key == key:
                    prev.next = cur.next

                    return cur
                else:
                    prev = prev.next
                    cur = cur.next

            return None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.items_stored = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.items_stored / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for char in key:
            hash = (hash * 33) + hash + ord(char)
        
        return (hash)


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        idx = self.hash_index(key)
        if self.data[idx] is None:
            self.data[idx] = LinkedList(HashTableEntry(key, value))
            self.items_stored += 1
        else:
            new_node = HashTableEntry(key, value)
            self.data[idx].insert_at_head(new_node)
            self.items_stored += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)

        if self.data[index] is None:
            print("Key not found")
            return

        deleted_node = self.data[index].delete(key)

        if deleted_node is not None:
            self.items_stored -= 1
            return deleted_node.value

        return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        if self.data[index] is not None:
            found_node = self.data[index].find(key)

            if found_node is not None:
                return found_node.value

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        if self.get_load_factor() > 0.7:
            # create new array with twice the current capacity
            new_storage = [None] * new_capacity
            self.capacity = new_capacity
            # loop thru self.data to find each entry
            for linked_list in self.data:
                if linked_list is not None:
                    cur = linked_list.head

                    while cur is not None:
                        # find new index for key and add node to new storage array
                        index = self.hash_index(cur.key)

                        if new_storage[index] is None:
                            new_storage[index] = LinkedList(
                                HashTableEntry(cur.key, cur.value))
                        else:
                            new_node = HashTableEntry(cur.key, cur.value)
                            new_storage[index].insert_at_head(new_node)

                        cur = cur.next

            self.data = new_storage



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
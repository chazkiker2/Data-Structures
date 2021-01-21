from doubly_linked_list.den_doubly_linked_list_02 import DoublyLinkedList, ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-key entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit  # max number of nodes
        self.current = 0  # current number of spaces taken in cache
        self.cache = None  # this will become a doubly-linked-list on first set()
        self.storage = {}  # this would be another Data Structure in full implementation
        # in full implementation storage would store the encryption for the key
        # and probably encryption for the data as well (at least some transformation of data)

    """
    Retrieves the key associated with the given key. Also
    needs to move the key-key pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the key associated with the key or None if the
    key-key pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            # trying to access key that exists in cache — move node to front if key exists in cache
            pointer = self.cache.head
            while pointer is not None:
                if pointer.key == key:
                    break

                else:
                    pointer = pointer.next

            self.cache.move_to_front(pointer)  # freshly accessed node goes to front
            return self.storage[key]  # just accessed

        else:  # nothing exists!
            return None

    """
    Adds the given key-key pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old key associated with the key with
    the newly-specified key.
    """

    def set(self, key, value):
        if key in self.storage:  # if key already exists in storage
            self.storage[key] = value  # overwrite key with new val
            pointer = self.cache.head  # cache is doubly-linked-list
            while pointer is not None:
                if pointer.key == key:
                    break

                else:
                    pointer = pointer.next

            self.cache.move_to_front(pointer)  # must pass in full node to move node to front

        else:
            if self.current == 0:  # if there is no cache
                # doubly linked list is slightly faster than single (multiple references)
                self.cache = DoublyLinkedList(ListNode(key))
                self.storage[key] = value  # first item in cache!
                self.current += 1  # add 1 to current slots taken

            elif self.current == self.limit:  # this will be fixed later
                removed_key = self.cache.remove_from_tail()  # removed old node from tail in doubly linked list
                del self.storage[removed_key]  # remove reference to old node in dictionary
                self.cache.add_to_head(key)  # add new node to head
                self.storage[key] = value  # overwrite the new key

            else:
                self.cache.add_to_head(key)  # add new key to beginning of doubly linked list
                self.storage[key] = value  # add reference to node in dictionary
                self.current += 1  # new slot occupied

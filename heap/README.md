# Stretch Goal: Heaps

## Heaps Overview

### Big-Picture
In computer science, a *heap* is a specialized tree-based data structure which is essentially an almost complete
tree that satisfies the heap property:

> In a _max heap_, for any given node `C`, if `P` is a parent node of `C`, then the _key_ (the _value_) of `P` is GREATER THAN or EQUAL TO the key of `C`.

> In a _min heap_, the key of `P` is less than or equal to the key of `C`. The node at the "top" of the heap (with no parents) is known as the _root_ node.

The heap is one maximally efficient implementation of an abstract data type called a priority queue. Priority queues are, in fact, often referred to as "heaps", regardless of how they may be implemented.
In a heap, the highest (or lowest) priority element is always stored at the root. However, a heap is not a sorted structure. It can be regarded as being partially ordered. A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority.

A common implementation of a heap is the binary heap, in which there is a binary tree. The heap data structure, specifically the binary heap, was introduced (by J. W. J. Williams in 1964) for the heapsort algorithm. 
Heaps are also crucial in several efficient graph algorithms such as Dijkstra's algorithm. When a heap is a complete binary tree, it has a smallest possible height — a heap with `N` nodes for each node `a` branches always has a log<sub>a</sub>(N) height.

Note that, as shown in the graphic, there is no implied ordering between siblings or cousins and no implied sequence for an *in-order traversal* (as there would be in, e.g., a binary search tree). Again: `binary search tree ≠ binary tree`. The heap relation mentioned above applies only between nodes and their parents, grandparents, etc. The max number of children each node can have depends on the type of heap!

### Expected Operations
The common operations involving heaps are as follows: 

##### Basic
 - `find_max` (or `find_min`): fina a maximum item of a max-heap or a minimum item of a min-heap, respectively. (a.k.a., `peek`)
 - `insert` add a new key to the heap (a.k.a., `push`)
 - `extract_max` (or `extract_min`): returns the node of maximum value from a max heap [or minimum value from a min heap] after removing it from the heap (a.k.a., `pop`)
 - `delete_max` (or `delete_min`): removing the root node of a max heap (or min heap), respectively
 - `replace`: `pop` root and `push` a new key. More efficient than a pop followed by a push, since the tree only needs to balance itself once rather than twice. Appropriate for fixed-size heaps.

##### Creation
 - `create_heap` —— create an empty heap
 - `heapify` —— create a heap out of a given array (list) of elements
 - `merge` (union) —— joining two heaps to form a valid new heap containing all the elements of both, preserving the original heaps
 - `meld` —— joining two heaps to form a valid new heap containing all the elements of both, destroying the original heaps.

##### Inspection
 - `size` —— return the number of items in the heap
 - `is_empty` —— return true if the heap is empty, false otherwise

##### Internal
 - `increase_key` or `decrease_key` —— updating a key within a max- or min- heap, respectively
 - `delete` —— delete an arbitrary node (followed by moving last node and sifting to maintain heap)
 - `sift_up` —— move a node up in the tree, as long as needed; used to restore heap condition after insertion. Called "sift" because node moves up the tree until it reaches the correct level, as in sieve.
 - `sift_down` —— move a node down in the tree, similar to `sift_up`; used to restore heap condition after deletion or replacement.


### Applications 
The heap data structure has many applications:
 - Heapsort: One of the best sorting methods being in-place with no quadratic worse-case scenarios. (very fucking cool)
 - Selection algorithms: A heap allows access to the min or max element in constant time, and other selections (such as median or kth-element) can be done sub-linear time on data that is in a heap.
 - Graph algorithms: By using heaps as internal traversal data structures, run-time will be reproduced by polynomial order. Examples of such problems are Prim's minimal-spanning-tree algorithm and Dijkstra's shortest-path algorithm.
 - Priority Queue: A priority queue is an abstract concept like "a list" or "a map"; just as a list can be implemented with a linked-list or an array, a priority queue can be implemented with a heap or a variety of other methods.
 - K-way merge: A heap data structure is useful to merge many already-sorted input streams into a single sorted output stream.
 - Order statistics: The heap data structure can be used to efficiently find the kth smallest (or largest) element in an array

## Max Heaps
* Should have the methods `insert`, `delete`, `get_max`, `_bubble_up`, and `_sift_down`.
  * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
  * `get_max` returns the maximum value in the heap _in constant time_.
  * `get_size` returns the number of elements stored in the heap.
  * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
  * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

![Image of a Heap in Tree form](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/501px-Max-Heap.svg.png)

![Image of a Heap in Array form](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Heap-as-array.svg/603px-Heap-as-array.svg.png)

## Generic Heaps
A max heap is pretty useful, but what's even more useful is to have our heap be generic such that the user can define their own priority function and pass it to the heap to use.

Augment your heap implementation so that it exhibits this behavior. If no comparator function is passed in to the heap constructor, it should default to being a max heap. Also change the name of the `get_max` function to `get_priority`.

You can test your implementation against the tests in `test_generic_heap.py`. The test expects your augmented heap implementation lives in a file called `generic_heap.py`. Feel free to change the import statement to work with your file structure or copy/paste your implementation into a file with the expected name.


## Sources
 - [Wikipedia — Heap (data structure)](https://en.wikipedia.org/wiki/Heap_(data_structure))

#!python


class BinaryMinHeap(object):
    """BinaryMinHeap: a partially ordered collection with efficient methods to
    insert new items in partial order and to access and remove its minimum item.
    Items are stored in a dynamic array that implicitly represents a complete
    binary tree with root node at index 0 and last leaf node at index n-1."""

    def __init__(self, items=None):
        """Initialize this heap and insert the given items, if any."""
        # Initialize an empty list to store the items
        self.items = []
        if items:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this heap."""
        return 'BinaryMinHeap({})'.format(self.items)

    def is_empty(self):
        """Return True if this heap is empty, or False otherwise."""
        # Check if empty based on how many items are in the list
        return self.size == 0

    def size(self):
        """Return the number of items in this heap."""
        return len(self.items)

    def insert(self, item):
        """Insert the given item into this heap.
        TODO: Best case running time: O(1) under what conditions? >> append at the end
        TODO: Worst case running time: O(logn) under what conditions? >> need to bubble up"""
        # Insert the item at the end and bubble up to the root
        self.items.append(item)
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def get_min(self):
        """Return the minimum item at the root of this heap.
        Best and worst case running time: O(1) because min item is the root."""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        return self.items[0]

    def delete_min(self):
        """Remove and return the minimum item at the root of this heap.
        TODO: Best case running time: O(1) under what conditions? >> if there is one item
        TODO: Worst case running time: O(n) n = height of the tree. under what conditions?"""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        elif self.size() == 1:
            # Remove and return the only item
            return self.items.pop()
        assert self.size() > 1
        min_item = self.items[0]
        # Move the last item to the root and bubble down to the leaves
        last_item = self.items.pop()
        self.items[0] = last_item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def replace_min(self, item):
        """Remove and return the minimum item at the root of this heap,
        and insert the given item into this heap.
        This method is more efficient than calling delete_min and then insert.
        TODO: Best case running time: O(1) under what conditions >> new item is the smallest element. no shift
        TODO: Worst case running time: O(n) under what conditions? >> new item is not the smallest element. n-height of the element"""
        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        min_item = self.items[0]
        # Replace the root and bubble down to the leaves
        self.items[0] = item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def _bubble_up(self, index):
        """Ensure the heap ordering property is true above the given index,
        swapping out of order items, or until the root node is reached.
        Best case running time: O(1) if parent item is smaller than this item.
        Worst case running time: O(log n) if items on path up to root node are
        out of order. Maximum path length in complete binary tree is log n."""
        if index == 0:
            return  # This index is the root node (does not have a parent)
        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))
        # Get the item's value
        item = self.items[index]
        # Get the parent's index and value
        parent_index = self._parent_index(index)
        parent_item = self.items[parent_index]
        # Swap this item with parent item if values are out of order
        if item < parent_item:
            self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
        # Recursively bubble up again if necessary
            index = self._parent_index(index)
            self._bubble_up(index)

    def _bubble_down(self, index):
        """Ensure the heap ordering property is true below the given index,
        swapping out of order items, or until a leaf node is reached.
        Best case running time: O(1) if item is smaller than both child items.
        Worst case running time: O(log n) if items on path down to a leaf are
        out of order. Maximum path length in complete binary tree is log n."""
        if not (0 <= index <= self._last_index()):
            raise IndexError('Invalid index: {}'.format(index))
        

        # if left_index > self._last_index():
        #     return  # This index is a leaf node (does not have any children)
        # Get the item's value
        item = self.items[index]
        # Get the index of the item's left and right children
        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)
        max_indx = index

        if left_index <= self._last_index() and self.items[left_index] < item:
            max_indx = left_index

        if right_index <= self._last_index() and self.items[right_index] < self.items[max_indx]:
            max_indx = right_index

        if max_indx != index:
            self.items[index], self.items[max_indx] = self.items[max_indx], self.items[index]
            if max_indx != len(self.items) - 1:
                self._bubble_down(max_indx)

    def _last_index(self):
        """Return the last valid index in the underlying array of items."""
        return len(self.items) - 1

    def _parent_index(self, index):
        """Return the parent index of the item at the given index."""
        if index <= 0:
            raise IndexError('Heap index {} has no parent index'.format(index))
        return (index - 1) >> 1  # Shift right to divide by 2

    def _left_child_index(self, index):
        """Return the left child index of the item at the given index."""
        return (index << 1) + 1  # Shift left to multiply by 2

    def _right_child_index(self, index):
        """Return the right child index of the item at the given index."""
        return (index << 1) + 2  # Shift left to multiply by 2


def test_binary_min_heap():
    # Create a binary min heap of 7 items
    items = [9, 25, 86, 3, 29, 5, 55]
    heap = BinaryMinHeap()
    print('heap: {}'.format(heap))

    print('\nInserting items:')
    for index, item in enumerate(items):
        heap.insert(item)
        print('insert({})'.format(item))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))
        heap_min = heap.get_min()
        real_min = min(items[: index + 1])
        correct = heap_min == real_min
        print('get_min: {}, correct: {}'.format(heap_min, correct))

    print('\nDeleting items:')
    for item in sorted(items):
        heap_min = heap.delete_min()
        print('delete_min: {}'.format(heap_min))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))


if __name__ == '__main__':
    test_binary_min_heap()

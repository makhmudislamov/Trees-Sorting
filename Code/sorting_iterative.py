#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: >>> O(n) because we have to iterate through the array. The bigger the array the longer it will take
    Memory usage: >>> O(1) because we are not creating extra space """

    # Declaring neighboring elements of items array
    previous_element = 0
    next_element = previous_element + 1

    while previous_element < len(items) - 1:
        # returning False at the first unsorted sequence
        if items[previous_element] > items[next_element]:
            return False
        previous_element += 1
        next_element += 1
    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: >>> O(n^2) because there is a loop inside a loop
    Memory usage: >>> O(1) because we are not creating new array but just modifying existing one"""
    
    while not is_sorted(items):
        # Declaring neighboring elements of items array and resetting after reaching the end of the array
        previous_element = 0
        next_element = previous_element + 1
        while previous_element < len(items) - 1:
            # returning False at the first unsorted sequence
            if items[previous_element] > items[next_element]:
                items[previous_element], items[next_element] = items[next_element], items[previous_element]
            previous_element += 1
            next_element += 1



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: >> O(n^2) loop inside a loop
    Memory usage: >> O(1) not creating new array"""

    
    j = 0
    i = 0
    min_index = 0

    while j < len(items):
        i = j + 1
        min_index = j

        while i < len(items):
            if items[i] < items[min_index]:
                min_index = i 
            i += 1

        items[j], items[min_index] = items[min_index], items[j]
        j += 1




def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


    sorted_start = 0
    unsorted = 1
    sorted_end = 0
    j = 0
    while unsorted < len(items): # iterating through unsorted part of the array

        # sorted_end = sorted_end - 1

        while sorted_start < len(items[:unsorted+1]): # trying to iterate through starte and end of the sorted sublist
            j = unsorted
            print(f"before comparison: j: {items[j]}, sorted_end: {items[sorted_end]}")
            if items[j] < items[sorted_end]:
                print(f"j: {items[j]}, sorted_end: {items[sorted_end]}")
                items[j], items[sorted_end] = items[sorted_end], items[j]
                sorted_end -= 1
                j -= 1

                print(f"after swap => j: {j}, sorted_end: {sorted_end}")
            else:  # found position
                print(f'items sorted left side: {items}')
                break
            if j == -1 or sorted_end == -1:
                break
            
                
        sorted_end = unsorted
        unsorted += 1

        
        

if __name__ == '__main__':
    items = [100, 2, 45, 3, 77, 15, 33]
    (insertion_sort(items))
    print(f"final items: {items}")

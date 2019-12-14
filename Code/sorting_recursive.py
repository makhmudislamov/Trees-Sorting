#!python


def merge(items_1, items_2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) - have to go through the whole array
    Memory usage: O(m) - we are creating new array which is exact size of the input"""

    # are the lists empty?
    if not items_1 and not items_2:
        return []

    # used to merge two sorted lists together
    merged_list = []
    index_1 = 0
    index_2 = 0

    # iterate until at least one of the lists are done
    while (index_1 < len(items_1)) and (index_2 < len(items_2)):
        
        if items_1[index_1] <= items_2[index_2]:
            merged_list.append(items_1[index_1])
            index_1 += 1
        else:
            merged_list.append(items_2[index_2])
            index_2 += 1

    # are there any elements left in items_1 list?
    if index_1 <= len(items_1)-1:
        # copy the rest of the elements from array items_1 to merged_list
        while index_1 < len(items_1):
            merged_list.append(items_1[index_1])
            index_1 += 1

    # are there any elements left in items_2 list?
    elif index_2 <= len(items_2)-1:
        # copy the rest of the elements from array items_2 to merged_list
        while index_2 < len(items_2):
            merged_list.append(items_2[index_2])
            index_2 += 1

    return merged_list



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n^2) - but depends on the sorting algo we are using.
    Memory usage: O(n) - we are creating new list at the end to merge"""
    # Split items list into approximately equal halves
    mid = len(items) // 2
    first_half = items[:mid]
    second_half = items[mid:]
    # Sort each half using any other sorting algorithm
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    # Merge sorted halves into one list in sorted order
    merged = merge(first_half, second_half)
    return merged


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(nlogn) - split, then split the splitted ....
    Memory usage: O(nlogn) - recursive stack"""
    # Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    else:
        # Split items list into approximately equal halves
        mid = len(items) // 2
        first_half = items[:mid]
        second_half = items[mid:]
        # Sort each half by recursively calling merge sort
        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)
        # Merge sorted halves into one list in sorted order
        return merge(first_half, second_half)


def find_median(items: list, low=None, high=None):
    """
    Find the median out of 3 numbers and swap the items in the list so median
    will be at the end of the list
    """
    # set the initial values of low and high
    if low == None and high == None:
        low = 0
        high = len(items) - 1

    mid = (high + low) // 2

    if items[mid] < items[low]:
        items[mid], items[low] = items[low], items[mid]
    if items[high] < items[low]:
        items[high], items[low] = items[low], items[high]
    if items[mid] < items[high]:
        items[mid], items[high] = items[high], items[mid]

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?"""
    # Choose a pivot any way and document your method in docstring above
    # Loop through all items in range [low...high]
    # Move items less than pivot into front of range [low...p-1]
    # Move items greater than pivot into back of range [p+1...high]
    # Move pivot item into final position [p] and return index
    print(f"low is {low}, high is {high}")

    if high - low >= 2:
        print(f"items before median: {items}")
        find_median(items, low, high)
        print(f"items after: {items}")

    # last element is the pivot
    pivot = items[high]
    pivot_index = low

    for i in range(low, high):
         # if there is smaller number than the pivot, swap it with pivot index
        if items[i] <= pivot:
            items[i], items[pivot_index] = items[pivot_index], items[i]
            # shift the pivot index to right
            pivot_index += 1

    # swap the pivot num from the end to the pivot index
    items[high], items[pivot_index] = items[pivot_index], items[high]

    return pivot_index
    


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

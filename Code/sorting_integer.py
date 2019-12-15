#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
   
    
    if not numbers:
        return []
    # Find range of given numbers (minimum and maximum integer values)
    start = min(numbers)
    end = max(numbers)
    # range of given numbers
    range_nums = end - start
    # Create list of counts with a slot for each number in input range
    counts = [0] * (range_nums + 1)
    # Loop over given numbers and increment each number's count
    for i, num in enumerate(numbers):  # O(n)
        # get the right index to increment
        index = num - start
        # increment the count of the number
        counts[index] += 1

    # Loop over counts and append that many numbers into output list
    output_list = []
    for i in range(len(counts)):  
        for _ in range(counts[i]):
            # redefine the number using the index of counts
            num = i + start
            output_list.append(num)
    # Improve this to mutate input instead of creating new output list
    numbers[:] = output_list
    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


if __name__ == "__main__":
    # test
    numbers = [12, 2, 45, 0, 1, 3]
    print(counting_sort(numbers))

numberOfCompMerge, numberOfSwapsMerge, counter = 0, 0, 0


def insertion_sort(collection):
    """
    Counts the number of comparisons (between two elements) and swaps
    between elements while performing an insertion sort

    :param collection: a collection of comparable elements
    :return: total number of comparisons and swaps
    """
    comparisons, swaps = 0, 0

    for x in range(1, len(collection)):
        # element currently being compared
        current = collection[x]

        # comparing the current element with the sorted portion and swapping
        while True:
            if x > 0 and collection[x - 1] > current:
                collection[x] = collection[x - 1]
                x -= 1
                collection[x] = current

                comparisons += 1
                swaps += 1
            else:
                comparisons += 1
                break

    return comparisons, swaps


def merge_sort(collection):
    """
    Counts the number of comparisons (between two elements) and swaps
    between elements while performing a merge sort

    :param collection: a collection of comparable elements
    :return: total number of comparisons and swaps, and the sorted list
    """
    comparisons, swaps = 0, 0
    mid = len(collection) // 2
    left, right = collection[:mid], collection[mid:]

    if len(left) > 1:
        left_result = merge_sort(left)
        comparisons += left_result[0]
        swaps += left_result[1]
        left = left_result[2]
    if len(right) > 1:
        right_result = merge_sort(right)
        comparisons += right_result[0]
        swaps += right_result[1]
        right = right_result[2]

    sorted_collection = list()

    # while elements in both sub lists
    while left and right:
        if left[0] <= right[0]:
            sorted_collection.append(left.pop(0))
        else:
            sorted_collection.append(right.pop(0))
        comparisons, swaps = comparisons + 1, swaps + 1

    # if elements are left in only one sublist, merge them (guaranteed sorted)
    if left:
        sorted_collection += left
        swaps += 1
    if right:
        sorted_collection += right
        swaps += 1

    return comparisons, swaps, sorted_collection


def print_results(comparisons, swaps, sorted_collection):
    print(f'Comparisons: {comparisons}'
          f'\nSwaps: {swaps}'
          f'\nSorted Collection: {sorted_collection}\n')


collections = []
for x in reversed(range(100)):
    collections.append(x)
comparison, swap = insertion_sort(collections)
print_results(comparison, swap, collections)


collections = []
for x in (range(100)):
    collections.append(x)
comparison, swap, result = merge_sort(collections)
print_results(comparison, swap, result)

collections = []
for x in (range(100)):
    collections.append(x)


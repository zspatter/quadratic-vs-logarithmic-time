numberOfCompMerge, numberOfSwapsMerge, counter = 0, 0, 0


def insertion_sort(collection):
    """
    Counts the number of comparisons (conditions checked) and swaps
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
    comparisons, swaps = 0, 0
    if len(collection) > 1:
        mid = len(collection) // 2
        left, right = collection[:mid], collection[mid:]

        left_part, right_part = merge_sort(left), merge_sort(right)
        comparisons += left_part[0] + right_part[0]
        swaps += left_part[1] + right_part[1]
        sorted_collection = list()

        while left and right:
            if left[0] < right[0]:
                sorted_collection.append(left.pop(0))
            else:
                sorted_collection.append(right.pop(0))
            comparisons, swaps = comparisons + 1, swaps + 1

        sorted_collection += (left or right)
        return comparisons, swaps, sorted_collection

        # while x < len(left) and y < len(right):
        #     if left[x] < right[y]:
        #         collection[z] = left.pop(0)
        #         x += 1
        #     else:
        #         collection[z] = right.pop(0)
        #         y += 1
        #
        #     comparisons += 1
        #     swaps += 1
        #     z += 1
        # # comparisons += 1
        #
        # while x < len(left):
        #     collection[z] = left[x]
        #     x += 1
        #     z += 1
        #
        #     # comparisons += 1
        #     # swaps += 1
        #
        # # comparisons += 1
        #
        # while y < len(right):
        #     collection[z] = right[y]
        #     y += 1
        #     z += 1

            # comparisons += 1
            # swaps += 1

        # comparisons += 1

    # else:
        # comparisons += 1

    # return comparisons, swaps


def mergesort(collection):
    comparisons, swaps = 0, 0
    mid = len(collection) // 2
    left, right = collection[:mid], collection[mid:]

    if len(left) > 1:
        left_result = mergesort(left)
        comparisons, swaps = comparisons + left_result[0], swaps + left_result[1]
        left = left_result[2]
    if len(right) > 1:
        right_result = mergesort(right)
        comparisons, swaps = comparisons + right_result[0], swaps + right_result[1]
        right = right_result[2]

    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        comparisons, swaps = comparisons + 1, swaps + 1
    result += (left or right)
    return comparisons, swaps, result


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
for x in reversed(range(100)):
    collections.append(x)
comparison, swap, result = merge_sort(collections)
print_results(comparison, swap, result)

collections = []
for x in reversed(range(100)):
    collections.append(x)
comparison, swap, result = mergesort(collections)
print_results(comparison, swap, result)
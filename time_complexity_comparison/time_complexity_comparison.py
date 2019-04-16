import copy
import csv
import time
import datetime


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
    # this does not count as swapping as it is just a copy operation
    #  no need for swap += len(left or right)
    sorted_collection += (left or right)

    return comparisons, swaps, sorted_collection


def read_csv(filename):
    data_set = list()
    with open(filename + '.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            for x in range(len(row)):
                try:
                    data_set.append(int(row[x]))
                except ValueError:
                    pass

    return data_set


def time_insertion_sort(data_set, iterations):
    counts, elapsed_time = list(), list()

    for _ in range(iterations):
        start_time = time.time_ns()
        counts.append(insertion_sort(copy.deepcopy(data_set)))
        end_time = time.time_ns()
        elapsed_time.append(end_time - start_time)

    return counts, elapsed_time


def time_merge_sort(data_set, iterations):
    counts, elapsed_time = list(), list()

    for _ in range(iterations):
        start_time = time.time_ns()
        comparisons, swaps, sorted_list = merge_sort(data_set)
        end_time = time.time_ns()
        counts.append((comparisons, swaps))
        elapsed_time.append(end_time - start_time)

    return counts, elapsed_time


def average_time(times):
    total_time = 0
    for element in times:
        total_time += element

    return int(total_time / len(times))


def run_comparison(filename, iterations):
    print(filename + ' comparison:')
    data_set = read_csv(filename)
    insertion_counts, insertion_times = time_insertion_sort(data_set, iterations)
    merge_counts, merge_times = time_merge_sort(data_set, iterations)

    print('Insertion Sort:')
    """unpack args for print_results()?"""
    print_results(insertion_counts, insertion_times)
    print('Merge Sort:')
    print_results(merge_counts, merge_times)


def print_results(counts, times):
    counts = list(zip(*counts))
    print(f'\tRun times: {times}')
    print(f'\tAverage: {average_time(times): ,d}')
    print(f'\tComparisons: {counts[0]}')
    print(f'\tSwaps: {counts[1]}\n')


start = datetime.datetime.now()
run_comparison('1k_ints', 10)
run_comparison('10k_ints', 10)
run_comparison('100k_ints', 10)
run_comparison('1000k_ints', 2)
run_comparison('100k_sequential_ints', 10)
end = datetime.datetime.now()
diff = end - start
print(f'Total elapsed time for this comparison: {diff}')

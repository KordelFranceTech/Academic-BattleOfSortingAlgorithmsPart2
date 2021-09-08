# quicksort.py
# Kordel France
########################################################################################################################
# This file provides functions to sort an array of integers in ascending order using a two-way merge sort.
########################################################################################################################
import time

QS_COMP = 0
QS_EX = 0

def partition_array(qArray, start_index, end_index):
    """
    Determines which point to partition the array at for the next epoch of quicksorting.
    :param qArray: the array to partition from.
    :param start_index: the index to start the array sort at
    :param end_index: the index to end the array sort at
    :return pivot_index: the specific index to pivot for the next partition..
    """
    global QS_COMP
    global QS_EX
    pivot_index = start_index
    pivot_point = start_index + 1

    for i in range(start_index + 1, end_index + 1):
        if qArray[i] <= qArray[pivot_index]:
            QS_COMP += 1
            qArray[pivot_point], qArray[i] = qArray[i], qArray[pivot_point]
            QS_EX += 1
            pivot_point += 1
    qArray[pivot_index], qArray[pivot_point - 1] = qArray[pivot_point - 1], qArray[pivot_index]
    QS_EX += 1
    pivot_index = pivot_point - 1
    return pivot_index


def quicksort(qArray, start_index, end_index):
    """
    Actually implements this style of the quicksort algorithm.
    It is the main routine called during recursion.
    :param qArray: the array to split and merge sort from.
    :param start_index: the index to start the array sort at
    :param end_index: the index to end the array sort at
    :return qArray: the sorted array.
    """
    if (start_index < end_index):
        partition_index = partition_array(qArray, start_index, end_index)
        quicksort(qArray, start_index, partition_index - 1)
        quicksort(qArray, partition_index + 1, end_index)
    # print(qArray)
    return qArray


def quicksort_driver(data_arr):
    """
    Driver for implementing vanilla quicksort.
    :param data_arr: the array to split and merge sort from.
    ;return data_arr: the sorted array.
    ;return QS_COMP: number of comparisons performed
    ;return QS_EX: number of exchanges performed
    ;return time: The time it takes for the algorithm to sort the file.
    """
    start_time = time.time()
    global QS_COMP
    global QS_EX

    qArray_sorted = quicksort(data_arr, 0, len(data_arr) - 1)

    end_time = time.time()
    delta_time = end_time - start_time
    return qArray_sorted, QS_COMP, QS_EX, "{:.6f}".format(delta_time)


def reset_counts_quicksort():
    """
    Resets the comparisons and exchanges counters so they are initialized for a new sort.
    """
    # reset comparison and exchange counts for next run
    global QS_COMP
    global QS_EX
    QS_COMP = 0
    QS_EX = 0


# q = [3, 3, 4, 4, 5, 6, 7, 45, 32, 76, 54, 65]
# quicksort(q, 0, len(q) - 1)


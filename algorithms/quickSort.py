def quickSort(arr):
    """
    Implements the Quick Sort algorithm.
    Selects a pivot and divides the list into sublists smaller and greater than the pivot.

    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def bubbleSort(arr):
    """
    Implements the Bubble Sort algorithm.
    Repeatedly traverses the list, swapping adjacent elements if they are in the wrong order.

    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

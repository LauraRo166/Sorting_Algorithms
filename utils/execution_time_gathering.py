import time
import pandas as pd
from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.mergeSort import mergeSort
from algorithms.quickSort import quickSort
from data_generator.generator import randomList

def measure_execution_time(algorithm, data):
    """
    Measures the execution time of a sorting algorithm.

    :param algorithm: Sorting function.
    :param data: List to be sorted.
    :return: Execution time in seconds.
    """
    start_time = time.time()
    algorithm(data.copy())
    return time.time() - start_time

def gather_execution_times(min_size, max_size, step, samples_per_size):
    """
    Collects execution times for different input sizes.

    :param min_size: Minimum list size.
    :param max_size: Maximum list size.
    :param step: Step size for increasing list size.
    :param samples_per_size: Number of samples per size.
    :return: Pandas DataFrame with execution times.
    """
    results = []

    for size in range(min_size, max_size + 1, step):
        for _ in range(samples_per_size):
            data = randomList(size)
            results.append({
                'Size': size,
                'BubbleSort': measure_execution_time(bubbleSort, data),
                'InsertionSort': measure_execution_time(insertionSort, data),
                'MergeSort': measure_execution_time(mergeSort, data),
                'QuickSort': measure_execution_time(quickSort, data)
            })

    return pd.DataFrame(results).groupby("Size", as_index=False).mean()
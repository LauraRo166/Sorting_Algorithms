# Sorting Algorithms
The following sorting algorithms are implemented:
+ Linear
+ Binary
+ Ternary

## Complexities Analysis

### Bubble Sort
+ Best Case (O(n)): If the array is already sorted, only one pass is needed.
+ Worst Case (O(n²)): If the array is sorted in reverse order, every element must be swapped in each iteration.
+ Average Case (O(n²)): On average, each element needs to be compared with half of the other elements.

### Insertion Sort
+ Best Case (O(n)): If the array is already sorted, each element is compared once and inserted without shifting.
+ Worst Case (O(n²)): If the array is sorted in reverse order, each element must be shifted n times.
+ Average Case (O(n²)): Each element is inserted by shifting half of the preceding elements on average.

### Merge Sort
+ Best Case (O(n log n)): Even if the array is already sorted, it still needs to be split and merged.
+ Worst Case (O(n log n)): The algorithm always divides the array into halves and merges them in sorted order.
+ Average Case (O(n log n)): The number of operations remains logarithmic due to the divide-and-conquer approach. 

### Quick Sort
+ Best Case (O(n log n)): If the pivot always divides the array into equal halves, the recursion depth is minimized.
+ Worst Case (O(n²)): If the pivot is always the smallest or largest element, the recursion depth is maximized.
+ Average Case (O(n log n)): On average, the pivot divides the array into reasonably balanced partitions.

## Unit and coverage testing


## Test and visualization
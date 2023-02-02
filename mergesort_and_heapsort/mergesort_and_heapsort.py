# ================================================================ #
# Mariana Zamudio Ayala
# Program that compares the execution time of the algorithms
# mergesort and heapsort using an array of len n.
# ================================================================ #
import math
import random
import time
import statistics
# ---------------------------------------------------------------- #
# Function that generates an array with the numbers from 1 to n
#  of random order and with uniform probability.
#   Input:
#       * n: length of the array (int)
#   Output:
#       * random_array
# ---------------------------------------------------------------- #
def create_random_array(n):
    # Create ordered array with numbers from 1 to n
    array = []
    for i in range(1, n + 1):
        array.append(i)
    # Swap numbers in array randomly
    for i in range(n):
        num_random = random.randint(0,n-1)
        array[i], array[num_random] = array[num_random], array[i]
    return array

def merge_sort(array):
    if len(array) > 1:
        # Find middle of the array and divide the array in two parts
        middle = math.floor(len(array) / 2)
        left = array[:middle]
        right = array[middle:]
        # Apply merge sort to each part of the array
        left = merge_sort(left)
        right= merge_sort(right)
        # Merge both arrays
        array = merge(array, left, right)
    return array

def merge(array, left, right):
    i = 0
    j = 0
    k = 0
    # Iterate until one of the array gets consumed
    while i < len(left) and j < len(right):
        # Add the smallest number to the array, and increase the counter
        # used to iterate the corresponding array.
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    # Add the remaining items to the array
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


def max_heapify(array, n, i):
    # Initialize the index that contains the largest number as the current item
    largest = i
    # Find the index for items to the left and right of i
    l = 2 * i + 1
    r = 2 * i + 2
    # Find the idex for the largest item (between the items left, right and i)
    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r
    # If the largest item is not i, then interchange the i and the larger one.
    # Also apply max_heapify to the largest
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, n, largest)

    return A

def build_max_heap(A):
    # Find the size of the heap
    heap_size = len(A)
    # Determine the index for the first item in the penultimate level of the tree
    s = heap_size//2
    # Start applying maxheapify to all items in the tree that are on the
    # penultimate level or higher
    for i in range(s,-1,-1):
        max_heapify(A,heap_size,i)
    return A

def heap_sort(A):
    # Order the tree (max number in the root)
    build_max_heap(A)
    # Find initial size of the heap
    heap_size = len(A)

    for i in range(len(A)-1,0,-1):
        # Place the maximum item to the end of the heap, and the last item to the beginning
        A[0], A[i] = A[i], A[0]
        # Decrease heap size as the last item is not needed (it is already in the corresponding place)
        heap_size -=1
        # Order the heap again, to get the maximum item at the root
        max_heapify(A,heap_size,0)
    return A


# MAIN
if __name__ == '__main__':
    merge_sort_time = []
    heap_sort_time = []
    arrays = []
    # Order 100 different arrays
    for i in range(100):
        # Create random array of size 100 000
        A = create_random_array(10000)
        arrays.append(A)
        # Start time counter for merge sort
        start_ms = time.time()
        # Call merge-sort algorithm
        print(merge_sort(A))
        # Stop time counter for merge sort
        end_ms = time.time()
        # Calculate execution time in seconds
        ex_time_ms = (end_ms - start_ms)
        merge_sort_time.append(ex_time_ms)

        # Start time counter for heap sort
        start_hs = time.time()
        # Call heap sort algorithm
        print(heap_sort(A))
        # Stop time counter for heap sort
        end_hs = time.time()
        # Calculate execution time in seconds
        ex_time_hs = (end_hs - start_hs)
        heap_sort_time.append(ex_time_hs)

    # Initialize array to store time data for each execution
    all_data = []
    for i in range(len(heap_sort_time)):
        encapsulated_data = [i, merge_sort_time [i],heap_sort_time[i]]
        all_data.append(encapsulated_data)
    # Print time data in table format
    print("{:<10} {:<20} {:<20}".format('execution', 'merge-sort', 'heap-sort'))
    print("-------------------------------------------------------------------")
    for data in all_data:
        exec, merge, heap = data
        print("{:<10} {:<20} {:<20}".format(exec, merge, heap))


    print("promedio mergesort:", statistics.mean(merge_sort_time))

    print("promedio heapsort:", statistics.mean(heap_sort_time))


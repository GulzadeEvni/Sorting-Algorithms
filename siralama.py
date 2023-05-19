import random
import time
import sys
sys.setrecursionlimit(10**6)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = random_partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def random_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l : m + 1]
    R = arr[m + 1 : r + 1]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def measure_time():
    sizes = [1000, 10000, 50000, 100000, 500000 , 1000000]
    
    for size in sizes:
        arr_random = [random.randint(0, size) for _ in range(size)]
        arr_sorted = list(range(size))
        arr_reverse = list(range(size, 0, -1))
        
        print(f"Dizi Boyutu: {size}")
        print("-" * 40)
        
        #Bubble Sort
        arr_copy = arr_random.copy()
        start_time = time.time()
        bubble_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Bubble Sort-Random: {execution_time:.6f} saniye")

        # Bubble Sort
        arr_copy = arr_sorted.copy()
        start_time = time.time()
        bubble_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Bubble Sort-Sıralı Dizi: {execution_time:.6f} saniye")

        # Bubble Sort
        arr_copy = arr_reverse.copy()
        start_time = time.time()
        bubble_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Bubble Sort-Ters Sıralı Dizi: {execution_time:.6f} saniye")


        
        # Selection Sort
        arr_copy = arr_random.copy()
        start_time = time.time()
        selection_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Selection Sort-Random: {execution_time:.6f} saniye")

        # Selection Sort
        arr_copy = arr_sorted.copy()
        start_time = time.time()
        selection_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Selection Sort-Sıralı Dizi: {execution_time:.6f} saniye")

        # Selection Sort
        arr_copy = arr_reverse.copy()
        start_time = time.time()
        selection_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Selection Sort-Ters Sıralı Dizi: {execution_time:.6f} saniye")
        


        # Insertion Sort
        arr_copy = arr_random.copy()
        start_time = time.time()
        insertion_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Insertion Sort-Random: {execution_time:.6f} saniye")

        # Insertion Sort
        arr_copy = arr_sorted.copy()
        start_time = time.time()
        insertion_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Insertion Sort-Sıralı Dizi: {execution_time:.6f} saniye")

        # Insertion Sort
        arr_copy = arr_reverse.copy()
        start_time = time.time()
        insertion_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Insertion Sort-Ters Sıralı Dizi: {execution_time:.6f} saniye")
        


        # Quick Sort
        arr_copy = arr_random.copy()
        start_time = time.time()
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Quick Sort-Random: {execution_time:.6f} saniye")

        # Quick Sort
        arr_copy = arr_sorted.copy()
        start_time = time.time()
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Quick Sort-Sıralı Dizi: {execution_time:.6f} saniye")

        # Quick Sort
        arr_copy = arr_reverse.copy()
        start_time = time.time()
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Quick Sort-Ters Sıralı Dizi: {execution_time:.6f} saniye")



        # Merge Sort
        arr_copy = arr_random.copy()
        start_time = time.time()
        merge_sort(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Merge Sort-Random: {execution_time:.6f} saniye")

        # Merge Sort
        arr_copy = arr_sorted.copy()
        start_time = time.time()
        merge_sort(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Merge Sort-Sıralı Dizi: {execution_time:.6f} saniye")

        # Merge Sort
        arr_copy = arr_reverse.copy()
        start_time = time.time()
        merge_sort(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Merge Sort-Ters Sıralı Dizi: {execution_time:.6f} saniye")



        
        # Heap Sort
        arr_copy = arr_random.copy()
        start_time = time.time()
        heap_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Heap Sort-Random: {execution_time:.6f} saniye")

         # Heap Sort
        arr_copy = arr_sorted.copy()
        start_time = time.time()
        heap_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Heap Sort-Sıralı Dizi: {execution_time:.6f} saniye")

         # Heap Sort
        arr_copy = arr_reverse.copy()
        start_time = time.time()
        heap_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Heap Sort-Ters Sıralı Dizi: {execution_time:.6f} saniye")
        


        # Shell Sort
        arr_copy = arr_random.copy()
        start_time = time.time()
        shell_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Shell Sort-Random: {execution_time:.6f} saniye")

        # Shell Sort
        arr_copy = arr_sorted.copy()
        start_time = time.time()
        shell_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Shell Sort-Sıralı Dizi: {execution_time:.6f} saniye")

        # Shell Sort
        arr_copy = arr_reverse.copy()
        start_time = time.time()
        shell_sort(arr_copy)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Shell Sort-Ters Sıralı Dizi: {execution_time:.6f} saniye")
        
        print()

measure_time()

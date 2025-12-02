import random
import time

# Generate 500 unique random numbers
data = random.sample(range(1, 10000), 500)

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

start_bubble = time.perf_counter()
sorted_bubble = bubble_sort(data)
end_bubble = time.perf_counter()
bubble_time = end_bubble - start_bubble

start_insertion = time.perf_counter()
sorted_insertion = insertion_sort(data)
end_insertion = time.perf_counter()
insertion_time = end_insertion - start_insertion

print("\n Sorting Algorithm Comparison:")
print(f"Bubble Sort Time:    {bubble_time:.6f} seconds")
print(f"Insertion Sort Time: {insertion_time:.6f} seconds")

preview = sorted_bubble[:5] + ["..."] + sorted_bubble[-5:]
print("\n Bubble Sorted Output:")
print(preview)

preview2 = sorted_insertion[:5] + ["..."] + sorted_insertion[-5:]
print("\n Insertion Sorted Output:")
print(preview2)

print("\n Efficiency Comparison:")
if bubble_time < insertion_time:
    print(" Bubble Sort is faster than Insertion Sort.")
elif insertion_time < bubble_time:
    print(" Insertion Sort is faster than Bubble Sort.")
else:
    print(" Both sorting algorithms took the same time.")

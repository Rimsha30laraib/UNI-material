import random
import time

# Step 1: Generate 499 unique random numbers
data = random.sample(range(1, 10000), 499)

print("\nGenerated Numbers (first 5 and last 5 shown):")
print(data[:5], "...", data[-5:])

target = int(input("\nEnter a number to search (between 1 and 9999): "))

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

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_insertion = insertion_sort(data)

start_linear = time.perf_counter()
linear_index = linear_search(data, target)
end_linear = time.perf_counter()
linear_time = end_linear - start_linear

start_binary = time.perf_counter()
binary_index = binary_search(sorted_insertion, target)
end_binary = time.perf_counter()
binary_time = end_binary - start_binary

print(f"Target Number: {target}")
print("\n Searching Algorithm Comparison:")
print(f"Linear Search: Index = {linear_index}, Time = {linear_time:.10f} seconds")
print(f"Binary Search: Index = {binary_index}, Time = {binary_time:.10f} seconds")

if linear_index == -1:
    print("Number not found using Linear Search.")
else:
    print("Number found using Linear Search.")

if binary_index == -1:
    print("Number not found using Binary Search.")
else:
    print("Number found using Binary Search.")

print("\n Efficiency Comparison:")
if linear_time < binary_time:
    diff = binary_time - linear_time
    print(f"Linear Search is faster by {diff:.10f} seconds.")
elif binary_time < linear_time:
    diff = linear_time - binary_time
    print(f"Binary Search is faster by {diff:.10f} seconds.")
else:
    print("Both searches took the same time.")

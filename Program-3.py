# Implement Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    smaller_elements = [x for x in arr if x < pivot]
    equal_elements = [x for x in arr if x == pivot]
    larger_elements = [x for x in arr if x > pivot]
    return quick_sort(smaller_elements) + equal_elements + quick_sort(larger_elements)
my_list = [8,7,3,9,1,6,4,5,2]
sorted_list = quick_sort(my_list)
print(sorted_list)

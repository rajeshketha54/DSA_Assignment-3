# Implement Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low<=high:
        mid=(low+high)//2 
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
    return "Not found" 
arr = [2,4,6,8,10,12,14,16,18,20]
target = 12
result = binary_search(arr,target)
if result == "Not found":
    print("Element not found")
else:
     print("Element {} found at index {}".format(target,result))


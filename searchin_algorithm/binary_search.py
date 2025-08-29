def binary_search(arr, target):
    left , right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target in arr[mid]:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [ 'apple', 'orange', 'watermelon', 'banana', 'kiwi', 'onion']  
    
    target = 'o'
    search_item = binary_search(arr, target)
    print(search_item)      
def linear_search(arr: list, target):
    found_items = []
    for i in range(len(arr)):
        if target in arr[i]:
            found_items.append(arr[i])
    if not found_items:
        return []
    return found_items          




if __name__ == "__main__":
    arr: list = ['apple', "mango", 'kiwi', 'banana', 'watermelon'];
    target = "o"    
    found_items = linear_search(arr, target)
    
    if not found_items:
        print("Item not found")
        
    for item in found_items:
        print(item)
    
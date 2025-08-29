def remove_duplicates(arr: list) -> list:
    unique_items: list = []
    for i in range(len(arr)):
        if arr[i] not in unique_items:
            unique_items.append(arr[i])
    return unique_items

def remove_duplicates_sort(arr: list) -> list:
    arr.sort()
    result: list = [arr[0]]
    for i in range(1, len(arr)):
        previous = i -1
        if arr[i] != arr[previous]:
            result.append(arr[i])
    return result
        
if __name__ == "__main__":
    arr: list = ["apple", 'banana', 'orange', 'watermelon', 'apple', 'apple', 'grapes'];
    filtered_list : list = remove_duplicates(arr)
    print(filtered_list)       
    print(remove_duplicates_sort(arr=arr)) 
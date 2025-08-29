def sort(numbers: int) -> None:
    for i in range(1, len(numbers)):
        start = numbers[i]
        j = i - 1
        while j >= 0 and  numbers[j] > start:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = start    
        
        
if __name__ == "__main__" :
    numbers: list = [12,4,34,53,18];
    sort(numbers)
    print(numbers)   
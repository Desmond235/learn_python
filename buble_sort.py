def sort(numbers: list) -> None:
    for i in range(len(numbers)):
        for x in range(len(numbers) - i - 1):
            if numbers[x] > numbers[x + 1]:
                temp: int = numbers[x + 1] 
                numbers[x + 1] = numbers[x]
                numbers[x] = temp
                
if __name__ == "__main__":
    numbers: list = [12,4,34,53,18];
    sort(numbers)
    print(numbers)                
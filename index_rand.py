import random


if __name__ == "__main__":
    index: str = "0021502178"
    last_three_digits = index[7:]
    base__num = int(last_three_digits)

    rand_numbers: list = []

    print(f"Index Number: {index}\n")

    for x in range(20):
        rand_number = random.randint(100, base__num) + base__num
        rand_numbers.append(rand_number)

    for i in range(1, len(rand_numbers)):
        key: int = rand_numbers[i]
        j = i -1
        while j >= 0 and rand_numbers[j] < key:
            rand_numbers[j + 1] = rand_numbers[j]
            j -= 1
        rand_numbers[j + 1] = key

    print("Sorted (descending)")
    print("********************")
    for x in range(len(rand_numbers)):
        print(rand_numbers[x])

    with open("C:/Users/HP/Desktop/PSORTEDTXT.txt", mode="a") as file:
        file.write("Sorted numbers (Descending)\n")
        file.write("***************************\n")
        for x in range(len(rand_numbers)):
            file.write(f"{rand_numbers[x]}\n")
    file.close()

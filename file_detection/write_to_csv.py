import  csv
import os

def write_to_csv(file, row):
    writer = csv.writer(file)
    writer.writerow(row)

def main():
    headers = ["Name", "Age", "Job"]
    name = input("Enter name: ")
    employees = []
    file_path = "Employee.csv"
    file_exists = os.path.exists(file_path)

    while not  name.isalpha():
        print('Please enter alphabets only')
        name = input("Enter name:")

    if name.isalpha():
        employees.append(name)

    age = input("Enter age: ")
    while not age.isdigit():
        print("Enter correct age: ")
        age = input("Enter age: ")

    if age.isdigit():
        employees.append(age)

    job = input("Enter job description: ")

    while not job.isalpha():
        print("Enter a correct job description")
        job = input("Enter job description: ")

    if job.isalpha():
        employees.append(job)
        print(employees)

    with open(file_path, "a", newline="") as file:
        if not  file_exists:
            write_to_csv(file, headers)
            print(f"Headers written to '{file_path}' successfully")
        write_to_csv(file, employees)

if __name__ == "__main__":
    main()
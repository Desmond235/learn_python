
import  json
import csv
# employees = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "Cook"
# }
#
# file_path = "output.json"
#
# try:
#     with open(file_path,'w') as file:
#         json.dump(employees,file, indent=4)
#         print(f"json file '{file_path}' created successfully")
# except FileExistsError:
#     print(f"txt file '{file_path}' already exists")

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist" ]
]
file_path = "output.csv"

try:
    with open(file_path,'w', newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)

        print(f"json file '{file_path}' created successfully")
except FileExistsError:
    print(f"txt file '{file_path}' already exists")
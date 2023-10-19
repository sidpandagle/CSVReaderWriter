import csv

# Reading a csv file
# with open('writesample.csv','r') as file:
#     csvReader = csv.reader(file)
#     for row in csvReader:
#         print(row)


# Write a csv file
row_list = [
    ["SNo", "Name", "Subject"],
    [1, "Ash Ketchum", "English"],
    [2, "Gary Oak", "Mathematics"],
    [3, "Brock Lesner", "Physics"],
]

with open("writesample1.csv", "w", newline="") as file:
    csvWriter = csv.writer(file, delimiter="|")
    csvWriter.writerows(row_list)

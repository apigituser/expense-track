import csv
import sys
import os
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
rows = [[1,timestamp,"Dinner",20],
        [2,timestamp,"New Watch",30],
        [3,timestamp,"Takeout",40],
        [4,timestamp,"Coffee",5]]

# ID Date Description Amount
def read_csv():
    with open("expenses.csv") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

def write_csv():
    with open("expenses.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    file_exists = os.path.isfile("expenses.csv")
    
    if file_exists:
        write_csv()
        read_csv()
    else: 
        print("File not found")
        exit(1)

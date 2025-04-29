import csv
import os
import sys
import argparse
import datetime

def list_expenses():
    with open("expenses.csv") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

def add_expense():
    if(os.stat("expenses.csv").st_size == 0):
        with open("expenses.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in rows:
                writer.writerow(row)
    else:
        with open("expenses.csv", "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            
def delete_expense():
    return

def summarise():
    return

if __name__ == "__main__":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    parser = argparse.ArgumentParser()
    parser.add_argument('--id')
    parser.add_argument('--month')
    parser.add_argument('--description')
    parser.add_argument('--amount')
    args = parser.parse_args()

    file_exists = os.path.isfile("expenses.csv")

    action = sys.argv[1]
    if file_exists:
        match action:
            case "add":
                add_expense()
            case "list":
                list_expenses()
            case "delete":
                delete_expense()
            case "summary":
                summarise()
    else: 
        print("File not found")
        exit(1)

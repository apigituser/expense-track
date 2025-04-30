import csv
import os
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
            writer.writerow([1, date, args.description, args.amount])
            print(f"Expense added successfully (ID:1)")
    else:
        with open("expenses.csv", "a", newline='') as csv_file:
            id = entries + 1
            writer = csv.writer(csv_file)
            writer.writerow([id, date, args.description, args.amount])
            print(f"Expense added successfully (ID:{id})")
            
def delete_expense():
    id = args.id
    with open("expenses.csv", "r+") as csv_file:
        reader = csv.reader(csv_file)
    print(f"Expense deleted (ID:{id})")

def summarise():        
    with open("expenses.csv") as csv_file:
        reader = csv.reader(csv_file)
        print(f"Total expenses: ${sum([int(row[3]) for row in reader])}")

if __name__ == "__main__":
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['list','add','summary','delete'])
    parser.add_argument('--id')
    parser.add_argument('--month')
    parser.add_argument('--description')
    parser.add_argument('--amount')
    args = parser.parse_args()

    file_exists = os.path.isfile("expenses.csv")
    if file_exists:
        with open("expenses.csv") as csv_file:
            reader = csv.reader(csv_file)
            entries = sum(1 for row in reader)

        match args.action:
            case 'list':
                list_expenses()
            case 'add':
                add_expense()
            case 'summary':
                summarise()
            case 'delete':
                delete_expense()
    else: 
        print("File not found")
        exit(1)
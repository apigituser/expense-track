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

def parse_args():
    parser = argparse.ArgumentParser("Track your expenses")
    subparsers = parser.add_subparsers(dest="action", help="Specify operation to be performed")

    list_parser = subparsers.add_parser(name="list", help="Display the expenses")

    add_parser = subparsers.add_parser(name="add", help="Record a new expense")
    add_parser.add_argument("-d", "--description", metavar="TEXT", required=True, help="Describe the expense")
    add_parser.add_argument("-a", "--amount", metavar="DOLLARS", required=True, help="Specify the amount spent")
    
    delete_parser = subparsers.add_parser(name="delete", help="Remove an expense")
    delete_parser.add_argument("-i", "--id", metavar="INTEGER", required=True, help="Specify the expense id to be removed")

    summary_parser = subparsers.add_parser(name="summary", help="Summarise your expenses")
    summary_parser.add_argument("-m", "--month", metavar="INTEGER", help="Specify a month (1-12)")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    args = parse_args()
    
    match args.action:
        case 'list':
            list_expenses()
        case 'add':
            add_expense()
        case 'summary':
            summarise()
        case 'delete':
            delete_expense()
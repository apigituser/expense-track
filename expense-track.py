import csv
import os
import argparse
import datetime
import tabulate

def list_expenses():
    with open("expenses.csv") as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
        headers = ('ID','Date','Description','Amount')
        table = tabulate.tabulate(data, headers=headers, colalign=('center','center','center','center'), tablefmt='fancy_grid')
        print(table)

def add_expense():
    entries = 1
    if file_exists:
        with open("expenses.csv", "a+", newline='') as file:
            file.seek(0)
            reader = csv.reader(file)
            entries = len([row for row in reader])
            id_ = entries + 1
            writer = csv.writer(file)
            writer.writerow([id_, date, args.description, args.amount])
            print(f"Expense added successfully (ID:{id_})")
            return 0
    with open("expenses.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([entries, date, args.description, args.amount])
        print(f"Expense added successfully (ID:{entries})")

def delete_expense():
    with open("expenses.csv", "r+", newline='') as file:
        reader = csv.reader(file)
        expenses = []
        exists = False
        for row in reader:
            if row[0] == args.id:
                exists = True
            else:
                expenses.append(row)
        if exists:
            file.seek(0)
            file.truncate()
            writer = csv.writer(file)
            writer.writerows(expenses)
            print(f"Expense deleted (ID:{args.id})")
        else:
            print(f"Expense with ID {args.id} not found")

def summarise():
    with open("expenses.csv") as file:
        reader = csv.reader(file)
        summarisedExpenses = [row for row in reader]
        if args.month:
            iso = datetime.date.fromisoformat
            file.seek(0)
            summarisedExpenses = [row for row in reader if iso(row[1]).month == args.month]
    print(f"Total Expenses: ${sum([int(row[3]) for row in summarisedExpenses])}")

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
    summary_parser.add_argument("-m", "--month", type=int, choices=range(1,13), metavar="INTEGER", help="Specify a month (1-12)")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    args = parse_args()

    file_exists = os.path.isfile("expenses.csv")

    match args.action:
        case 'list':
            if file_exists: list_expenses()
        case 'summary':
            if file_exists: summarise()
        case 'delete':
            if file_exists: delete_expense()
        case 'add':
            add_expense()
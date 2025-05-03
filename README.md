# Expense Track CLI
Expense Tracker CLI tool to track your expenses

## Prerequisites
Clone this repository using the following command
  ```
  git clone https://github.com/apigituser/expense-track
  ```
Install tabulate using pip
  ```
  pip install tabulate
  ```

## Functions
1. List expenses
2. Add expense
3. Delete expense
4. Summarise expenses

## Usage

### List Expenses
  ```
  python expense-track list
  ```
### Add an expense
  ```
  python expense-track add --description <DESC> --amount <AMOUNT>
  ```
### Delete an expense
  ```
  python expense-track delete --id <ID>
  ```
### Summarise expenses (Total)
  ```
  python expense-track summary
  python expense-track summary --month <1-12>
  ```
## Roadmap.sh Project URL
Project link is available [here](https://roadmap.sh/projects/expense-tracker)

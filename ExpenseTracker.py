# -*- coding: utf-8 -*-

import os
import csv
import datetime
import matplotlib.pyplot as plt


def add_money():
    deposit = int(input("Enter the amount you wish to deposit: "))
    global income
    income += deposit
    print("Income added: ", income)

expense_sheet='data.csv'
def enter_data():
    if not os.path.exists(expense_sheet):
        with open(expense_sheet, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Label', 'Expense'])

    if os.path.exists(expense_sheet):
        read_file_list = list(csv.reader(open(expense_sheet, 'r')))
        if len(read_file_list) == 0:
            with open(expense_sheet, 'a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Label', 'Expense'])

    date = int(input("Enter the date (dd): "))
    label = input("Label your Expense: ")
    expense = int(input("Expense amount:"))

    with open(expense_sheet, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, label, expense])


def choices():
    print("0 : Add income to the account.")
    print("1 : Enter the expenses.")
    print("2 : Raw insights of data.")
    print("3 : Graphical view of current data.")
    print("4 : Graphical view for a particular date range")

    try:
        choice = int(input())
    except Exception as e:
        print("!Enter a valid Value..", e)

    return choice


def data_insights():
    try:
        with open(expense_sheet, 'r') as file:
            read = csv.reader(file)
            read_list = list(read)
            print(read_list)
            total_expense = 0

            if income <= 0:
                print("!! You don't have any income yet. Add some amount first.");
                return

            for each in read_list[1:]:
                total_expense += int(each[2])

            balance = income - total_expense
            print("Account Balance:", balance)
            print("Total Expenditure this month:", total_expense)
            percent = (total_expense / income * 100)
            print("Expenditure is {:.4f}%  of income in {} days of this month.\n".format(percent, len(read_list) - 1))
    except Exception as e:
        print("It looks like you don't have enough data yet to visualize.", e)


def data_visualization():
    try:
        with open(expense_sheet, 'r') as file:
            dates = []
            expense = []
            read = csv.reader(file)
            file_list = list(read)
            for each in file_list[1:]:
                dates.append(int(each[0]))
                expense.append(int(each[2]))

            today = datetime.date.today()

            plt.bar(dates, expense, label='per month')
            plt.title("--Monthly Expenditure--")
            plt.xlabel(f"Date {today.month} {today.year}")
            plt.ylabel("Expense")
            plt.xlim([1, 15])
            plt.legend()
            plt.show()
    except Exception as e:
        print("It looks like you don't have enough data yet to visualize.", e)


def limited_visualization(start_date, end_date):
    try:
        with open(expense_sheet, 'r') as file:
            dates = []
            expense = []
            read = csv.reader(file)
            file_list = list(read)
            # print(len(file_list))
            if end_date > (len(file_list) - 1):
                print("!! End date out of range..")
                return

            for each in file_list[start_date:end_date + 1]:
                dates.append(int(each[0]))
                expense.append(int(each[2]))
            total_expense = sum(list(map(int, expense)))
            percent = total_expense / income * 100
            print(f"Total expenditure in this period is {total_expense} which is {percent:.4f}% of the monthly income.")
            today = datetime.date.today()
            plt.plot(dates, expense, label='per day range')
            plt.title("--Range of days Expenditure--")
            plt.xlabel(f"Date {today.month} {today.year}")
            plt.ylabel("Expense")
            plt.xlim([1, 15])
            plt.xticks(dates)
            plt.legend()
            plt.show()
    except Exception as e:
        print("It looks like you don't have enough data yet to visualize.", e)


if __name__ == "__main__":
    income = 0

    print("Select the choice::")
    running = True
    while running:
        choice = choices()
        if choice == 0:
            add_money()
        elif choice == 1:
            enter_data()
        elif choice == 2:
            data_insights()
        elif choice == 3:
            data_visualization()
        elif choice == 4:
            print("Specify:")
            start = int(input("Start Date: "))
            end = int(input("End Date: "))
            limited_visualization(start, end)
        else:
            print("!!INVALID choice.")

        ask = input("Do you want to continue:(y/n) ")
        if ask == 'n' or ask == 'N':
            running = False

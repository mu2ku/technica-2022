import csv

def check_credit_rating(credit_score):
    '''return true if buyer is approved (credit score >= 640) and false otherwise'''
    if credit_score >= 640:
        return True
    return False

def loan_to_value(loan_amount, down_payment, monthly_payment):
    return (loan_amount - down_payment) / loan_amount
    

def check_front_end_debt_to_income(monthly_mortgage, gross_monthly_income):
    '''return true if buyer is approved (fedti <= 28) and false otherwise'''
    ratio = monthly_mortgage/gross_monthly_income * 100
    if ratio <= 28:
        return True
    return False

def is_approved(row):
    return 

with open("technica_2022-HomeBuyerInfo.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
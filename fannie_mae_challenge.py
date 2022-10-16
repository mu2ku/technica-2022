import csv
import os

def check_credit_rating(credit_score):
    '''return true if buyer is approved (credit score >= 640) and false otherwise'''
    # print(credit_score)
    if float(credit_score) >= 640:
        return True
    return False

def check_loan_to_value(loan_amount, appraised_value):
    loan_amount = float(loan_amount)
    appraised_value = float(appraised_value)
    ratio = loan_amount/appraised_value * 100
    if ratio < 80:
        return True
    return False

def check_debt_to_income(debt, gross_monthly_income, mortgage):
    gross_monthly_income = float(gross_monthly_income)
    mortgage = float(mortgage)
    ratio = (debt+mortgage)/gross_monthly_income * 100
    if ratio <= 36:
        return True
    return False

def check_front_end_debt_to_income(monthly_mortgage, gross_monthly_income):
    '''return true if buyer is approved (fedti <= 28) and false otherwise'''
    monthly_mortgage = float(monthly_mortgage)
    gross_monthly_income = float(gross_monthly_income)
    ratio = monthly_mortgage/gross_monthly_income * 100
    if ratio <= 28:
        return True
    return False

def is_approved(row):
    return check_credit_rating(row[9]) and check_loan_to_value(row[7], row[5]) and check_debt_to_income(float(row[2])+float(row[3])+float(row[4]), row[1], row[8]) and check_front_end_debt_to_income(row[8], row[1])

def why_not_approved(row):
    str = ""
    if check_credit_rating(row[9]) == False:
        if len(str) == 0:
            str += "credit score too low"
        else:
            str += " and credit score too low"
    if check_loan_to_value(row[7], row[5]) == False:
        if len(str) == 0:
            str += "LTV too high"
        else:
            str += " and LTV too high"
    if check_debt_to_income(float(row[2])+float(row[3])+float(row[4]), row[1], row[8]) == False:
        if len(str) == 0:
            str += "DTI too high"
        else:
            str += " and DTI too high"
    if check_front_end_debt_to_income(row[8], row[1]) == False:
        if len(str) == 0:
            str += "FEDTI too high"
        else:
            str += " and FEDTI too high"
    return str

data = []
header = ["ID", "GrossMonthlyIncome", "CreditCardPayment", "CarPayment", "StudentLoanPayments", "AppraisedValue", "DownPayment", "LoanAmount", "MonthlyMortgagePayment", "CreditScore", "ApprovedOrNot", "WhyNotApproved"]

def process_csv(path, name):
    with open(path, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            if row[0] == 'ID':
                pass
            elif is_approved(row):
                row.append('Y')
                row.append('approved')
                data.append(row)
            else:
                row.append('N')
                row.append(why_not_approved(row))
                data.append(row)

    output_file = f'{name}_PROCESSED.csv'
    with open(os.path.join('output', output_file), 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        for item in data:
            csvwriter.writerow(item)
    return output_file
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3, csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////db.sqlite3"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employee", methods=['GET', 'POST'])
def employee_page():
    return render_template("employee.html")

@app.route("/customer")
def customer_page():
    return render_template("customer.html")

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        gross_monthly_income = request.form['monthly_income']
        credit_card_payment = request.form['credit_card_payment'] 
        car_payment = request.form['car_payment'] 
        student_loan = request.form['student_loan_payment']
        appraised_value = request.form['appraised_value']
        down_payment = request.form['down_payment'] 
        loan_amount = request.form['loan_amount']
        monthly_mortage = request.form['monthly_mortgage'] 
        credit = request.form['credit_score'] 
        
        con = sqlite3.connect("test.db")
        cur = con.cursor() #establish cursor
        print("Connected to SQLite")
        
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT, gross_monthly_income, credit_card_payment, car_payment, student_loan, appraised_value, down_payment, loan_amount, monthly_mortage, credit)")
        
        cur.execute("""INSERT INTO test (gross_monthly_income, credit_card_payment, car_payment, student_loan, appraised_value, down_payment, loan_amount, monthly_mortage, credit) VALUES (?,?,?,?,?,?,?,?,?)""",(gross_monthly_income, credit_card_payment, car_payment, student_loan, appraised_value, down_payment, loan_amount, monthly_mortage, credit))
        con.commit()  
        con.close()
        
        return render_template("index.html")

@app.route('/addbatch', methods=['POST','GET'])
def addbatch():
    if request.method == 'POST':
        f = request.files['file']
        
        con = sqlite3.connect("test.db")
        cur = con.cursor() #establish cursor
        print("Connected to SQLite")
        
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT, gross_monthly_income, credit_card_payment, car_payment, student_loan, appraised_value, down_payment, loan_amount, monthly_mortage, credit)")
        
        insert_query = """INSERT INTO test (gross_monthly_income, credit_card_payment, car_payment, student_loan, appraised_value, down_payment, loan_amount, monthly_mortage, credit) VALUES (?,?,?,?,?,?,?,?,?)""" 
        
        for row in f:
            print(row)
            # cur.execute(insert_query,row[1:])
            # con.commit()
            # con.close()      
            
        return render_template("index.html")
                
if __name__ == "__main__":
    app.run(debug=True)
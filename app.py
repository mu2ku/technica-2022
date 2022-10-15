from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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

if __name__ == "__main__":
    app.run(debug=True)
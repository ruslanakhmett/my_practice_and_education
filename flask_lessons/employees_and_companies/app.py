from flask import Flask, render_template

from data import generate_table

table = generate_table(employees_count=30, companies_count=10)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employees/')
def employees():
    employees = table['employees']
    employees = sorted(employees, key=lambda e: e['name'])
    return render_template('employee/index.html', employees=employees)


@app.route('/companies/')
def companies():
    companies = table['companies']
    companies = sorted(companies, key=lambda c: c['name'])
    return render_template('company/index.html', companies=companies)


@app.route('/employees/<int:id>')
def get_employee(id):
    companies = table['companies']
    employees = table['employees']
    
    employee = next(e for e in employees if e['id'] == id)
    employee_company = next(c for c in companies if c['id'] == employee['company'])  # noqa: E501
    return render_template(
        'employee/show.html',
        employee=employee,
        employee_company=employee_company
    )

@app.route('/companies/<int:id>')
def get_company(id):
    companies = table['companies']
    employees = table['employees']

    company = next(c for c in companies if c['id'] == id)
    company_employees = [employee for employee in employees if employee['company'] == id]  # noqa: E501
    return render_template(
        'company/show.html',
        company=company,
        company_employees=company_employees
    )
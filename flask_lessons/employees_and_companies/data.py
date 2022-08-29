import random

from faker import Faker

SEED = 1234


def generate_employees(employees_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(employees_count))
    random.seed(SEED)
    random.shuffle(ids)
    employees = []
    for i in range(employees_count):
        employee = fake.profile(fields=['name', 'username', 'address', 'mail'])
        employee['id'] = ids[i]
        employees.append(employee)
    return employees


def generate_companies(companies_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(companies_count))
    random.seed(SEED)
    random.shuffle(ids)

    companies = []
    for i in range(companies_count):
        company = {
            'name': fake.company(),
            'id': ids[i],
            'employees': [],
        }
        companies.append(company)
    return companies


def add_employees_to_companies(employees, companies):
    for i, employee in enumerate(employees):
        company = companies[i % len(companies)]
        employee['company'] = company['id']
        company['employees'].append(employee['id'])
    return employees, companies


def generate_table(employees_count, companies_count):
    employees = generate_employees(employees_count)
    companies = generate_companies(companies_count)
    employees, companies = add_employees_to_companies(employees, companies)
    return {
        'employees': employees,
        'companies': companies,
    }

import pandas as pd
from os import system
from salary_register.employees import Employee, MONTHS
from salary_register.utils import get_employee_name, get_month_choice, data_to_xlsx
from salary_register.data import register


def main():
    employees: list[Employee] = []
    number_of_employees = Employee.get_number_of_employees()
    range_of_employees = range(number_of_employees)
    system('cls')

    for employee_number in range_of_employees:
        employee_name = get_employee_name(employee_number=employee_number)
        employees.append(Employee(name=employee_name))

    for month in MONTHS:
        system('cls')
        employees_data: list[pd.DataFrame] = []
        will_resister_current_month = get_month_choice(month)

        if not will_resister_current_month:
            continue

        for employee in employees.copy():
            system('cls')
            if not employee.will_be_registered(employees, month):
                continue
            employee.register_salary(month)
            if employee.got_a_bonus(month):
                employee.register_bonuses(month)
            if employee.did_overtime(month):
                if employee.got_custom_overtime_rate():
                    employee.change_overtime_rate(month)
                employee.register_overtime_salary(month)

            employees_data.append(register(current_month=month, employee=employee))

        data_to_xlsx(current_month=month, employees_data=employees_data)


if __name__ == "__main__":
    main()

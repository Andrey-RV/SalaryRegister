from .employees import Employee
import pandas as pd


def register(current_month: str, employee: Employee) -> pd.DataFrame:
    """_Creates a DataFrame with the employee's data for the current month._

    Args:
        current_month (str): _A string with the current month._
        employee (Employee): _An employee object._

    Returns:
        pd.DataFrame: _A DataFrame with the employee's data for the current month._
    """
    employee_data: dict[str, str | float] = {
        "Name": employee.name,
        "Base salary": employee.salary[current_month],
        "Monday to Saturday overtime hours": employee.overtime1_hours[current_month],
        "Overtime salary from Monday to Saturday": employee.overtime1_salary[current_month],
        "Monday to Saturday overtime rate": employee.overtime1_rate[current_month],
        "Sunday and Holidays overtime hours": employee.overtime2_hours[current_month],
        "Overtime salary from Sunday and Holidays": employee.overtime2_salary[current_month],
        "Sunday and Holidays overtime rate": employee.overtime2_rate[current_month],
        "Bonuses": "Yes" if employee.bonuses[current_month] else "No",
        "Bonuses values": employee.bonuses_value[current_month] if employee.bonuses[current_month] else 0.0
    }
    return pd.DataFrame([employee_data])

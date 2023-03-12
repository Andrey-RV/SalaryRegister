import os
import pandas as pd
from typing import MutableSequence


def get_employee_name(employee_number: int) -> str:
    """_Handles the input of the employee name.

    Args:
        employee_number (int): _A number that represents the current employee._

    Returns:
        str: _Returns the employee name._
    """
    employee_name = input(f"Enter the name of the employee {employee_number + 1}: ")
    while employee_name[0] == '-' or employee_name.isdigit() or len(employee_name) < 1:
        employee_name = input("Invalid input. Please insert a real name (not numbers or only one letter): ")
    return employee_name


def get_month_choice(current_month: str) -> bool:
    """_Handles the input of the month choice and checks if the user wants to register the salaries of the current month.

    Args:
        current_month (str): _A string with the current month._

    Returns:
        bool: _Wether the user wants to register the salaries of the current month or not._
    """
    will_resister_current_month = input(f"\nDo you want to register the salaries of {current_month}? (Y/N): ")

    while will_resister_current_month.upper() not in ['Y', 'N']:
        will_resister_current_month = input("Invalid input. Try again: ")

    if will_resister_current_month.upper() == 'N':
        return False
    else:
        return True


def data_to_xlsx(current_month: str, employees_data: MutableSequence[pd.DataFrame]) -> None:
    """_Saves the data to an excel file. Every month's data is saved in a different sheet of the same file._

    Args:
        current_month (str): _A string with the current month._
        employees_data (MutableSequence[pd.DataFrame]): _A sequence with data of the employees. Every employee's data must be a DataFrame._
    """
    file_name = 'salary_register.xlsx'

    if employees_data:
        data = pd.concat(employees_data, ignore_index=True)  # type: ignore
    else:
        data = pd.DataFrame()

    if os.path.isfile(file_name):
        with pd.ExcelWriter(file_name, mode='a') as writer:
            data.to_excel(writer, sheet_name=current_month, index=False)  # type: ignore
    else:
        with pd.ExcelWriter(file_name, mode='w') as writer:
            data.to_excel(writer, sheet_name=current_month, index=False)  # type: ignore

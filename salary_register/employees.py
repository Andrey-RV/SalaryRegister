from typing import MutableSequence


MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")


class Employee:
    def __init__(self, name: str) -> None:
        """Initialize an employee object.

        Args:
            name (str): The employee's name.
        """
        self.name = name
        self.salary: dict[str, float] = {}
        self.bonuses: dict[str, float] = {}
        self.bonuses_value: dict[str, float] = {}
        self.overtime1_hours: dict[str, float] = {}
        self.overtime2_hours: dict[str, float] = {}
        self.overtime1_salary: dict[str, float] = {}
        self.overtime2_salary: dict[str, float] = {}
        self.overtime1_rate = {"January": 1.5, "February": 1.5, "March": 1.5, "April": 1.5, "May": 1.5,  "June": 1.5,
                               "July": 1.5, "August": 1.5, "September": 1.5, "October": 1.5, "November": 1.5, "December": 1.5, }
        self.overtime2_rate = {"January": 2.0, "February": 2.0, "March": 2.0, "April": 2.0, "May": 2.0, "June": 2.0,
                               "July": 2.0, "August": 2.0, "September": 2.0, "October": 2.0, "November": 2.0, "December": 2.0, }

    @staticmethod
    def get_number_of_employees() -> int:
        """Get the number of employees to be registered.

        Returns:
            int: The number of employees to be registered.
        """
        employee_quantity = input("How many employees will be registered? ")

        while not employee_quantity.isdigit() or employee_quantity[0] == '-':
            employee_quantity = input("Please, insert a positive number of employees: ")

        return int(employee_quantity)

    def will_be_registered(self, employees: MutableSequence['Employee'], current_month: str) -> bool:
        """Check if the employee will be registered for the month.

        Args:
            employees (MutableSequence): A sequence of employee objects.
            current_month (str): The month currently being registered.

        Returns:
            bool: Whether the employee will be registered for the month or not.
        """
        employee_will_be_registered = input(f'Do you want to register {self.name} for {current_month}? "Y" or "N": ')

        while employee_will_be_registered.upper() not in ("Y", "N"):
            employee_will_be_registered = input('Please, insert "Y" or "N": ')

        if employee_will_be_registered.upper() == 'N':
            employee_status = input("Is the employee fired? 'Y' or 'N': ")

            while employee_status.upper() not in ("Y", "N"):
                employee_status = input('Please, insert "Y" or "N": ')

            if employee_status.upper() == 'Y' and self in employees:
                employees.remove(self)
            return False

        else:
            return True

    def register_salary(self, current_month: str) -> None:
        """Register the employee's base salary for the month.

        Args:
            current_month (str): The month currently being registered.
        """
        if self.salary:
            self._update_salary(current_month)

        elif not self.salary:
            salary = input("\nWhat is the base salary of the employee? (digits only) ")

            while not salary.isdigit() or salary[0] == '-':
                salary = input("Please, enter a positive number: ")

            self.salary[current_month] = float(salary)

    def _update_salary(self, current_month: str) -> None:
        """Check if the employee's base salary will be updated for the month. If so, updates it.

        Args:
            current_month (str): The month currently being registered.
        """
        previous_month = MONTHS[MONTHS.index(current_month) - 1]

        if self.salary.get(previous_month) is None:
            print("There is no previous month data about the salary.")
            base_salary_will_be_changed = 'Y'
        else:
            base_salary_will_be_changed = input('Do you want to change the current base salary of' +
                                                f' {self.salary.get(previous_month)}? "Y" or "N": ')

        while base_salary_will_be_changed.upper() not in ("Y", "N"):
            base_salary_will_be_changed = input('Please, insert "Y" or "N": ')

        if base_salary_will_be_changed.upper() == 'Y':
            salary = input("Enter the new base salary (digits only): ")

            while not salary.isdigit() or salary[0] == '-':
                salary = input("Please, enter a positive number: ")

            self.salary[current_month] = float(salary)

        else:
            self.salary[current_month] = self.salary[previous_month]

    def got_a_bonus(self, current_month: str) -> bool:
        """Check if the employee got a bonus for the month.

        Args:
            current_month (str): The month currently being registered.

        Returns:
            bool: Whether the employee got a bonus for the month or not.
        """
        bonus = input(f"\nDid {self.name} got a bonus this month? 'Y' or 'N': ")

        while bonus.upper() not in ("Y", "N"):
            bonus = input('Please, insert "Y" or "N": ')

        if bonus.upper() == "Y":
            self.bonuses[current_month] = True
            return True
        else:
            self.bonuses[current_month] = False
            return False

    def register_bonuses(self, current_month: str) -> None:
        """Register the bonus value for the month.

        Args:
            current_month (str): The month currently being registered.
        """
        bonus_value = input("\nHow much was the bonus? (digits only): ")

        while not bonus_value.isdigit() or bonus_value[0] == '-':
            bonus_value = input("Please, enter a positive number: ")

        bonus_value_float = float(bonus_value)
        self.bonuses_value[current_month] = bonus_value_float

    def did_overtime(self, current_month: str) -> bool:
        """Check if the employee did overtime for the month.

        Args:
            current_month (str): The month currently being registered.

        Returns:
            bool: Whether the employee did overtime for the month or not.
        """
        employee_did_overtime = input(f"\nDid {self.name} work overtime this month? 'Y' or 'N': ")

        while employee_did_overtime.upper() not in ("Y", "N"):
            employee_did_overtime = input('Please, insert "Y" or "N": ')

        if employee_did_overtime == "Y":
            return True
        else:
            self.overtime1_hours[current_month] = 0
            self.overtime1_salary[current_month] = 0
            self.overtime1_rate[current_month] = 0
            self.overtime2_hours[current_month] = 0
            self.overtime2_salary[current_month] = 0
            self.overtime2_rate[current_month] = 0
            return False

    @staticmethod
    def got_custom_overtime_rate() -> bool:
        """Checks if the overtime rate will be changed for the month.

        Returns:
            bool: Whether the overtime rate will be changed for the month or not.
        """
        overtime_rate_will_be_changed = input('By default, the overtime rate is 50% for weekdays and 100% for weekends and holidays.' +
                                              ' Do you want to change it? "Y" or "N": ')

        while overtime_rate_will_be_changed.upper() not in ("Y", "N"):
            overtime_rate_will_be_changed = input('Please, insert "Y" or "N": ')

        if overtime_rate_will_be_changed == "Y":
            return True
        else:
            return False

    def change_overtime_rate(self, current_month: str) -> None:
        """Change the overtime rate for the month.

        Args:
            current_month (str): The month currently being registered.
        """
        custom_rate1 = input('Enter the overtime rate for weekdays' +
                             ' (an integer representing the percentage: 50 = 50%, thus 1.5 times the base salary): ')

        while (not custom_rate1.isdigit() or custom_rate1[0] == '-'):
            custom_rate1 = input("Please, enter a positive number: ")

        while float(custom_rate1) < 50:
            custom_rate1 = input("You are entering a value lower than the allowed. Please, enter a rate greater or equal than 50: ")

        custom_rate2 = input('Enter the overtime rate for weekdays' +
                             ' (an integer representing the percentage: 100 = 100%, thus 2 times the base salary): ')

        while not custom_rate2.isdigit() or custom_rate2[0] == '-':
            custom_rate2 = input("Please, enter a positive number: ")

        while float(custom_rate2) < 100:
            custom_rate2 = input("You are entering a value lower than the allowed. Please, enter a rate greater or equal than 100: ")

        self.overtime1_rate[current_month] = float(custom_rate1) / 100
        self.overtime2_rate[current_month] = float(custom_rate2) / 100

    def register_overtime_salary(self, current_month: str) -> None:
        """Register the overtime salary for the month.

        Args:
            current_month (str): The month currently being registered.
        """
        overtime_hour = input("\nHow many hours of overtime were done on weekdays? ")

        while not overtime_hour.isdigit() or overtime_hour[0] == '-':
            overtime_hour = input("Please, enter a positive number: ")

        self.overtime1_hours[current_month] = float(overtime_hour)

        overtime_hour2 = input("\nHow many hours of overtime were done on weekdays? ")

        while not overtime_hour2.isdigit() or overtime_hour2[0] == '-':
            overtime_hour2 = input("Please, enter a positive number: ")

        self.overtime2_hours[current_month] = float(overtime_hour2)

        overtime_salary1 = self.overtime1_rate[current_month] * (self.salary[current_month] / 220)
        overtime_salary2 = self.overtime2_rate[current_month] * (self.salary[current_month] / 220)
        self.overtime1_salary[current_month] = self.overtime1_hours[current_month] * overtime_salary1
        self.overtime2_salary[current_month] = self.overtime2_hours[current_month] * overtime_salary2

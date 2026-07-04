from datetime import datetime

class Staff():
    def __init__(self, first_name: str, last_name: str, phone: str, email: str, role: str, hire_date: datetime, salary: float):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.role = role
        self.hire_date = hire_date
        self.salary = salary

    def print_staff(self):
        print("\nPrint staff feature coming soon!")
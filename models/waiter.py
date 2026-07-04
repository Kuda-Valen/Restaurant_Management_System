from models.staff import Staff
from datetime import datetime

class Waiter(Staff):
    def __init__(self, first_name: str, last_name: str, phone: str, email: str, role: str, hire_date: datetime, salary: float, revenue: float, tips_accrued: float):
        super(). __init__(first_name, last_name, phone, email, role, hire_date, salary)
        self.revenue = revenue
        self.tips_accrued = tips_accrued

    def print_waiters(self):
        print("\nPrint Waiters feature coming soon!")
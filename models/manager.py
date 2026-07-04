from models.staff import Staff
from datetime import datetime

class Manager(Staff):
    def __init__(self, first_name: str, last_name: str, phone: str, email: str, role: str, hire_date: datetime, salary: float):
        super(). __init__(first_name, last_name, phone, email, role, hire_date, salary)
        
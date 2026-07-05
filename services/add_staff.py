from models.staff import Staff

def add_staff():
    print("\n -- Add staff -- \n")
    first_name = input("Enter Staff First Name: ").strip()
    last_name = input("Enter Staff Last Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    role = input("Enter Role: ").strip()
    hire_date = input("Enter Hire Date: ").strip()
    salary = input("Enter Salary: ").strip()

    staff = Staff(first_name, last_name, phone, email, role, hire_date, salary)
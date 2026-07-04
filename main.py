from services.login import authenticate
from services.add_staff import add_staff

def main_menu():
    while True:
        print("\n === Restaurant Management System === \n")
        print("1. Login")
        print("2. Add User")
        print("3. Exit")

        try:
            option = int(input("\nChoose an Option: "))

            if option == 1:
                authenticate()
            
            elif option == 2:
                add_staff()
            
            elif option == 3:
                print("Exiting...")
                return
            
            else:
                print("Invalid Input. Choose Valid Option.")
        
        except ValueError as e:
            print(f"\nAn Input Error Occured. Error: {e}")


if __name__ == "__main__":
    main_menu()
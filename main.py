# Employee Management System
# A simple program to add, view, search, update and delete employees.

# This list stores all employees. Each employee is a dictionary.
employees = []


def add_employee():
    emp_id = input("Enter ID: ")
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary,
    }
    employees.append(employee)
    print("Employee added!")


def view_employees():
    if len(employees) == 0:
        print("No employees yet.")
    else:
        for emp in employees:
            print(emp["id"], "|", emp["name"], "|", emp["department"], "|", emp["salary"])


def search_employee():
    emp_id = input("Enter ID to search: ")
    for emp in employees:
        if emp["id"] == emp_id:
            print("Found:", emp["name"], "|", emp["department"], "|", emp["salary"])
            return
    print("Employee not found.")


def update_employee():
    emp_id = input("Enter ID to update: ")
    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter new name: ")
            emp["department"] = input("Enter new department: ")
            emp["salary"] = input("Enter new salary: ")
            print("Employee updated!")
            return
    print("Employee not found.")


def delete_employee():
    emp_id = input("Enter ID to delete: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee deleted!")
            return
    print("Employee not found.")


# Main menu: keeps running until the user chooses Exit
while True:
    print("\n--- Employee Management System ---")
    print("1. Add employee")
    print("2. View all employees")
    print("3. Search employee")
    print("4. Update employee")
    print("5. Delete employee")
    print("6. Exit")

    choice = input("Choose (1-6): ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

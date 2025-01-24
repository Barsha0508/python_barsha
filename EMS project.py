import mysql.connector 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nidhi@123",
    database="employeemanagmentsystem"
)
cobj = db.cursor()
print("database connected sucessfully")

cobj.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    ID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Position VARCHAR(50),
    Salary FLOAT
)
""")
print("Table Created Successfully.\n")

cobj = db.cursor()
cobj.execute("CREATE DATABASE EmployeeManagemtSystem")

#print("Database 'EmpManagemtSystem' created successfully!")

#Create the Employee Table

# Add a New Emp
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Employee Department: ")
    position = input ("Enter Employee Position: ")
    salary = float(input("Enter salary: "))

    quary = "Insert into Employees (ID ,Name , Department,Position ,Salary) Values (%s,%s,%s,%s,%s)"
    values = (emp_id,name,department,position,salary)
    cobj.execute(quary, values)
    db.commit()
    print("Employee added  Successfully!\n")

#view all employee
def view_employee():
    cobj.execute("Select * from Employees ")
    Employees = cobj.fetchall()

    if not Employees:
                 print("Employee Not Found ")
                 return
    print("\n Employees List")
    print("--" * 50 +"\n")
    for emp in Employees:
        print(f"ID: {emp[0]} , Name: {emp[1]} , Department: {emp[2]} , Position: {emp[3]} , Salary: {emp[4]}")
    print("-" * 50 +"\n")

#Search For an Employee
def Search_employee():
    emp_id = input("Enter Employee ID to search: ")
    query = "SELECT * FROM Employees WHERE ID = %s"
    cobj.execute(query, (emp_id,))
    employee = cobj.fetchone()  # Note the capital 'E'

    if employee:  # Changed 'employee' to 'Employee'
        print(f"Employee found: ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}, Position: {employee[3]}, Salary: {employee[4]}")
    else:
        print("Employee not found.\n")

#update employee details
def Update_employee():
    emp_id = input("Enter Employee ID to update: ")
    query = "SELECT * FROM Employees WHERE ID = %s"
    cobj.execute(query, (emp_id,))
    Employee = cobj.fetchone()

    if not Employee:
        print("Employee Not Found")
        return
    
    name = input("Enter New Name: ")
    department = input("Enter new Department: ")
    position = input("Enter new Position: ")
    salary = float(input("Enter New Salary: "))

    update_query = '''
    UPDATE Employees
    SET Name = %s, Department = %s, Position = %s, Salary = %s
    WHERE ID = %s
    '''
    
    values = (name, department, position, salary, emp_id)
    cobj.execute(update_query, values)
    db.commit()
    print("Employee updated successfully!\n")

    
#Delete as employee
def delete_employee():
    emp_id = input("Enter Employee ID To delete ")
    query = "Delete from Employees where ID = %s"
    cobj.execute (query,(emp_id,))
    db.commit()

    if cobj.rowcount > 0:
        print("Employee  Delete Successfully!\n")
    else:
        print("Employee Not Found.\n")
#main Menu
def main():
    while True:
        print("\nEmployee Managment System")
        print(" 1. Add Employee:")
        print(" 2. View All Employees:")
        print(" 3. Search for an Employee:")
        print(" 4. Update Employee:")
        print(" 5. Delete Employee:")
        print(" 6. Exit")
        choice = input("Enter The Choice: ")

        if choice == "1":
             add_employee()
        elif choice == "2":
             view_employee()
        elif choice == "3":
             Search_employee()
        elif choice == "4":
             Update_employee()
        elif choice == "5":
             delete_employee()
        elif choice == "6":
             print("Exiting...")
             break
        else:
            print("Invalid choice")
if _name_ == "_main_":
    main()

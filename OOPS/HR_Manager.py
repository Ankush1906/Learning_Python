class Employee:
    def __init__(self, id, name, dept, salary):
        self.id = id
        self.name = name
        self.dept = dept
        self.salary = salary

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Department: {self.dept}, Salary: {self.salary}")


class HRManager(Employee):
    def __init__(self, id, name, dept, salary):
        super().__init__(id, name, dept, salary)
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show(self):
        print("Employee Details:")
        for emp in self.employees:
            emp.display()



hr = HRManager(1, "Ankush", "HR", 80000)

emp1 = Employee(101, "Ravi", "IT", 50000)
emp2 = Employee(102, "Rohan", "Finance", 60000)

hr.add_employee(emp1)
hr.add_employee(emp2)

hr.show()

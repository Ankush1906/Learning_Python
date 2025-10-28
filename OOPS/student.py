class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
    

class UG_Student(student):
    def __init__(self, name, roll_no,course):
        super().__init__(name, roll_no)
        self.course = course

    def show(self):
        self.display()
        print(f"course:{self.course}")

s1 = UG_Student("Ankush", 101, "btech")
s1.show()
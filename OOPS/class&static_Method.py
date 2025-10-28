class Student:

    dress = "white shirt and black pant"

    @classmethod
    
    def changedress(cls,new_dress):
        cls.dress = new_dress


    @staticmethod

    def behaviour():
        print("good behaviour")


    

Student.changedress("blue shirt and dark blue pant")

Student.behaviour()

print(Student.dress)


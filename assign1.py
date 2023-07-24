class Student:

    ls = []  # Class variable to store all student objects

    def __init__(self, name, roll, subjects):
        self.name = name
        self.roll = roll
        self.subjects = subjects

    @classmethod
    def add_student(cls, Name, Roll, Subjects):
        obj = Student(Name, Roll, Subjects)
        cls.ls.append(obj)

    @classmethod
    def display(cls, obj):
        print("Name : ", obj.name)
        print("RollNo : ", obj.roll)
        print("Subjects : ", obj.subjects)
        print("\n")

    @classmethod
    def search(cls, rn):
        for i in range(len(cls.ls)):
            if cls.ls[i].roll == rn:
                return i
        return -1

    @classmethod
    def delete(cls, rn):
        i = cls.search(rn)
        if i != -1:
            del cls.ls[i]
            print("Student with RollNo {} deleted.".format(rn))
        else:
            print("Student with RollNo {} not found.".format(rn))

    @classmethod
    def update(cls, rn, No):
        i = cls.search(rn)
        if i != -1:
            cls.ls[i].roll = No
            print("Student RollNo updated to {}.".format(No))
        else:
            print("Student with RollNo {} not found.".format(rn))

    def get_unique_subjects(self):
        all_subjects = set()
        for student in self.ls:
            all_subjects.update(student.subjects)
        return all_subjects


# Object of class
obj1 = Student('', 0, 0)

print("\nOperations used, ")
print("\n1.add Student details\n"
      "2.Display Student Details\n" 
       "3.Search Details of a Student\n"
        "4.Delete Details of Student" 
      "\n5.Update Student Details\n6.Exit")

obj1.add_student("A", 1, ["Hindi", "English", "Maths"])
obj1.add_student("B", 2, ["Hindi", "English"])
obj1.add_student("C", 3, ["Hindi", "English", "Science"])

print("\nList of Students\n")
for i in range(len(Student.ls)):
    obj1.display(Student.ls[i])

print("\nStudent Found, ")
s = obj1.search(2)
if s != -1:
    obj1.display(Student.ls[s])

obj1.delete(2)
print(len(Student.ls))
print("List after deletion")
for i in range(len(Student.ls)):
    obj1.display(Student.ls[i])

obj1.update(3, 2)
print(len(Student.ls))
print("List after updation")
for i in range(len(Student.ls)):
    obj1.display(Student.ls[i])

print("\nList of unique subjects studied by all students:")
unique_subjects = obj1.get_unique_subjects()
print(unique_subjects)

print("Thank You!")

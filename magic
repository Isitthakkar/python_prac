class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        marks = self.marks + other.marks
        return marks

    def __repr__(self):
        return 'Marks : {}'.format(self.marks)

    def __call__(self, value):
        self.marks = value
        print(self.marks)

    def __mul__(self, other):
        marks = self.marks * other.marks
        return marks

    def __lt__(self, other):
        if self.marks < other.marks:
            print('{} is less than {}'.format(self.marks, other.marks))
        else:
            print('{} is greater than {}'.format(self.marks, other.marks))


student1 = Student(20)
student2 = Student(40)

print(student1 + student2)

print(student1 * student2)

print(student1)
print(student2)

student1(70)
student2(90)

student1 < student2

class Student:

    def get(self):
        self.name = input("Enter name: ")
        self.branch = input("Enter branch: ")

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)



s1 = Student()


s1.get()
s1.display()

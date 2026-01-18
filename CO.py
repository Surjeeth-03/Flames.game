class sur:
    clg_name="SIST"
    def __init__(self):
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
    def dis(self):
        print(f"{self.name:^20} {self.age:^10} {self.clg_name:^10}")
        print()
no_of_students=int(input("Enter number of students: "))
l=[]
for i in range(1,no_of_students+1):
    x=sur()
    l.append(x)
print("_" * 40)
print(f"{'Name':^20} {'Age':^10} {'Clg':^10}")
print("_" * 40)
print()
for i in l:
    i.dis()
print("_" * 40)
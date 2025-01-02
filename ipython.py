# num1 = 10
# num2 = 20

# a = 10
# b = 20
# if a > b:
#     print("A is greater than B")
# else:
#     print("B is greater than A")

# 

# class Employee:
#     def __init__(self, name, age, salary, gender):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender

#     def show_employee_details(self):
#         print("Name of the employee is", self.name)
#         print("Age of the employee is", self.age)
#         print("Salary of the employee is", self.salary)
#         print("Gender of the employee is", self.gender)

# e1 = Employee("John", 35, 40000, "Male")
# e1.show_employee_details()



# class Vehicle:
#     def __init__(self, mileage, cost):
#         self.mileage = mileage
#         self.cost = cost

#     def show_vehicle_details(self):
#         print("The mileage of this vehicle is", self.mileage)
#         print("The cost of this vehicle is", self.cost)

# v1 = Vehicle(500, 1500)
# v1.show_vehicle_details()

# class Car (Vehicle):
#     def show_car_details(self):
#         print("I am a car")


# c1 = Car(200, 1000)
# c1.show_vehicle_details()
# c1.show_car_details()

# class Parent:
#     def assign_name(self,name):
#         self.name = name

#     def show_name(self):
#         return self.name

# class Child(Parent):
#     def assign_age(self,age):
#         self.age = age

#     def show_age(self):
#         return self.age

# class GrandChild(Child):
#     def assign_gender(self,gender):
#         self.gender = gender

#     def show_gender(self):
#         return self.gender

# gc = GrandChild()
# gc.assign_name("Ace")
# gc.assign_age(10)
# gc.assign_gender("Male")
# print(gc.show_name())
# print(gc.show_age())
# print(gc.show_gender())


# f = open('chim.txt', 'r')
# content = f.read()
# print(content)

# f = open('chim.txt','w')
# f.write('I am learning file handling')
# f.write("\nAnd python too")

# print(f.readline())
# f.close()

# f = open('chim.txt','a')
# append = f.write('\nI am learning to append')
# print(f)
# f.close()



# a = input("Enter the number 1: ")
# b = input("Enter the number 2: ")

# try:
#     if a > b:
#         print(a,"is greater than",b)
#         print(f"{a} is greater than {b}")
#     else:
#         print(b,"is greater than",a)
# except Exception as e:
#     print(e)
# finally:
#     print("Finally keyword used")
    

#Implementation using Queue
# from queue import LifoQueue
# stack = LifoQueue(maxsize=3)
# stack.put(2)
# stack.put(3)
# stack.put(4)
# print(stack.qsize())   #qsize gives the number of elements in the stack
# print(stack.full())    #full checks whether the stack is full or not

# #QUEUE DATA STRUCTURE (ENQUEUE- inserting AND DEQUEUE- deleting)
# class Queue:
#     def __init__(self):
#         self.queue []
#     def enqueue(self, item):
#         self.queue.append(item)
#     def dequeue(self):
#         if len(self.queue)<1:
#             return None
#         return self.queue.pop(0)
#     def display(self):
#         print(self.queue)
#     def size(self):
#         return len(self.queue)


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.display()
# q.dequeue()
# print(q.size())

#Linked List Pseudo code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

n1 = Node(8)
print(n1.data)
print(n1.next)

class Singly:
    def __init__(self):
        self.head = None
Singly()
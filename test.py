# print("Hello World")

# print("Hello", end=" World", flush=True)

x = 3
# y = 3.0
# z = "Hello"
# # x = z * y
# print(z + ", " + str(x))
# x = 3.0
# x = "Hello"
# def x(x):
#     print(x)
# x(x)

# def sum(a, b=10):
#     print(a)
#     return a + b

# print(sum(3,7))

# print(sum(5,4))
# print(x)

# x = 0
# y = 1

# if x < y < 2:
#     print("X is True")
# elif x == False:
#     print("X is False")
# else:
#     print("X is not a bool")

li = [] #list
# li = [1,2,3,4]
li.append(1)
li.append(2)
li.insert(0,3)
li += [4] #most useful
li = [5]+li
# print(li[1:3])

x = 0
# while x < len(li):
#     print(li[x])
#     x+=1

# for x in range(len(li)):
#     print(li[x])

# for x in li: #will use for DB models
#     print(x)

# x = (1,2,3) #tuple
# x += (4,2,4)

# print(x[0])

# x = {} #dictionary
# x = {"key": [{},{"Hi":"bob"},3]}
# x[0] = 3
# print(x["key"])





class Person:
    # member_var = "Hi"

    def __init__(self, name):
        # Initialize property
        self.age = 0
        # Assign the argument to the instance's name attribute
        self.name = name
        
    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, name, classification="Freshman"):
        super().__init__(name)
        self.classification = classification
        # Person.__init__(self, name)
    
    def get_class(self):
        return self.classification

bob = Student(name="Bob",classification="Junior")
# bob.set_age(50)
print(bob.get_name())





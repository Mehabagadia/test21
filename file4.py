#PYTHON BUILT-IN CLASS FUNCTION
class Student:
    def __init__(self, name, id ,age):
        self.name = name
        self.id = id
        self.age = age
s = Student("meha" , 202 ,19)        
print(getattr(s,'name'))
setattr(s ,"age",19)
print(getattr(s, 'age'))
print(hasattr(s,'id'))
delattr(s,'age')
#print(s.age)
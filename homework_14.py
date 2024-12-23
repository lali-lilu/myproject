class VectorClass:
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        # Multiplication operation
        if isinstance(other, (int, float)):
            return VectorClass(self.x * other, 
                               self.y * other, 
                               self.z * other)
        elif isinstance(other, VectorClass):
            return VectorClass(self.x * other.x, 
                               self.y * other.y, 
                               self.z * other.z)
    
    def __add__(self, other):
        # Addition operation
        if isinstance(other, (int, float)):
            return VectorClass(self.x + other, 
                               self.y + other, 
                               self.z + other)
        elif isinstance(other, VectorClass):
            return VectorClass(self.x + other.x, 
                               self.y + other.y, 
                               self.z + other.z)

    def __str__(self):
        # String representation
        return f"{self.x}:{self.y}:{self.z}"


# Input
x1 = int(input("შეიყვანეთ X1-ის მნიშვნელობა: "))
y1 = int(input("შეიყვანეთ Y1-ის მნიშვნელობა: "))
z1 = int(input("შეიყვანეთ Z1-ის მნიშვნელობა: "))

x2 = int(input("შეიყვანეთ X2-ის მნიშვნელობა: "))
y2 = int(input("შეიყვანეთ Y2-ის მნიშვნელობა: "))
z2 = int(input("შეიყვანეთ Z2-ის მნიშვნელობა: "))

tod = input("რა ოპერაციის ჩატარება გსურთ, მიმატება add,  თუ გამრავლება mul ?:  ")

v1 = VectorClass(x1, y1, z1)
v2 = VectorClass(x2, y2, z2)

# Perform the operation based on user input
if tod == "mul":
    v3 = v1 * v2  # This works as expected
    print("v3 (multiplication result) ->", v3)

elif tod == "add":
    v4 = v1 + v2  # This works as expected
    print("v4 (addition result) ->", v4)

# Optionally print v1 and v2 as well
print("v1 ->", v1)
print("v2 ->", v2)
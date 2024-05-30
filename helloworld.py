# run python -> python helloworld.py
print("hello world")

# phải có dấu cách thay vì dùng backet {}
if 5 > 2:
    print("5 lon hon 2")
    print("hellow")

# tạo biến    
x = 4
y = "string"
z = str(x) #casting (ép kiểu)
x = 'string ${x}'
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
fruits = ["apple", "banana", "cherry"]

#functions
x = "awesome" #đây là global scope
def myfunc():
  global x #khởi tạo global variable inside function
  print("Python is " + x)

myfunc()

#data types trong pythons
x = 1j #complex -> aka số phức
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry") #tuple -> khởi tạo và không thể thay đổi giá trị
coordinates = (10, 20)
person = ("Alice", 30, "Engineer")
print(coordinates[0])
    
x = range(6) #dict 
x = frozenset({"apple", "banana", "cherry"}) #frozenset
x = b"Hello" #bytes
x = bytearray(5) #bytes array
x = memoryview(bytes(5)) #memory view
x = None #none -> tương ứng với undefined,null 
print(type(x))


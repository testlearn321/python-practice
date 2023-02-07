def greet():
    print("hello")
    print("good morning")

greet()

def add(x,y):
    c=x+y
    print(c)
add(893,3)
add(8,7)


def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d
result1,result2=add_sub(5,6)
print(result1,result2)
def update(x):
    x=8
    print("x", x)

a=10                                            #passbyvalue
update(a)                                       #pass by reference
print("a",a)

def update(lst):
    print(id(lst))
    lst[1]=27
    print(id(lst))
    print("x",lst)

lst=[23,56,29]                                           #passbyvalue
print(id(lst))
update(lst)                                       #pass by reference
print("lst",lst)













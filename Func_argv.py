#Function
def greet():
    print("Hello")
greet()
#Default Arguments
def car(brand, model="Unknown", color="White"):
    print("Brand:", brand)
    print("Model:", model)
    print("Color:", color)
car("Toyota")
#Positional Arguments
def car(brand, model, price):
    print("Brand:", brand)
    print("Model:", model)
    print("Price:", price)
car("Toyota", "Innova", 2500000)
#Keyword Arguments
def car(brand, model, price):
    print("Brand:", brand)
    print("Model:", model)
    print("Price:", price)
car(price=2500000, model="Innova", brand="Toyota")
#orbitary Arguments
def greeting(*students):
    for i in students:
        print('hi',i,'Tomorrow is leave')
greeting('devi','sri','priya','sara')

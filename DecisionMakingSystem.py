#if statement
raining = True
if raining:
    print("Take an umbrella")
    
#if-else statement
money = 500
price = 400
if money >= price:
    print("You can buy the product")
else:
    print("You cannot buy the product")
    
#if-elif-else Statement
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Nested if Statement
hallticket = True
idcard = True
if hallticket:
    if idcard:
        print("You can enter the exam hall")
    else:
        print("Bring your ID card")
else:
    print("You need a hall ticket")

import random

c=random.randrange(1,101)
a=int(input("enter the number:"))
if a>c:
    print("Computer Number:",c)
    print("Your number is too high........")
elif c>a:
    print("computer number",c)
    print("Your number is too low.........")
else:
    print("computer number",c)
    print("Your number is equal.........")


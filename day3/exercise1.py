name=input("enter your name:")

if len(name) <3:
    print("name must be at least 3 character")
elif len(name) >50:
    print("name must be a max of 50 characters")
else:
    print("name looks good")
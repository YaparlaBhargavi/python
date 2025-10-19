guess=input("If you Want HELP type 'help':")
print(guess.lower())
guess='help'
if guess == "help":
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
choose=input("Choose 'start', 'stop' , 'quit':")
print (choose.lower())
if choose=='start':
   print("Car started....Ready to go!")
if choose=='stop':
    print("Car stopped.")
if choose =='quit':
    print("thank you")
   
   
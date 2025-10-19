weight=float(input("weight:"))
unit =input("(L)bs or (K)g:")
if unit.upper() == "L":
    converted=weight*0.45
    print(f"you are {converted} kilos")
elif unit.upper() =="K":
    converted=weight * 2.2
    print(f"you are {converted} pounds")
    
else:
    print("invalid unit entered.please enter 'L' or 'K'")
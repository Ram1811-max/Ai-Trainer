import UpperBodyModule as ubm
import LowerBodyModule as lbm
print("if you want to train for upperbody press 'u")
print("if you want to train for lowerbody press 'l")

ch=input("enter your choise : ")

if ch=='u':
    ubm.upperBody()
else:
    lbm.lowerBody()
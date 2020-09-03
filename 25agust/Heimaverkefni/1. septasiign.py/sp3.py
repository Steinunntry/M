first = int(input("Input the first integer: "))
second = int(input("Input the second integer: "))

#Let us assume that Python does not have a multiplication operator. 
#  Write a Python program that implements multiplication by using addition and a for loop

outcome = 0
for i in range(first):
    outcome += second
print(outcome)


    


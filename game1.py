import random
num = random.randint(1,21)
print(num)

for i in range(1,6): # 5 chances only
    user = int(input("enter the number:"))
    if user == num:
        print ("you won")
        break
        
    elif user > num:
        print("too high")
        
    elif user < num:
        print("too low")
name = input("Enter your name: ")
print("Welcome",name,"to this adventure!")

answer = input("You are on a dirt road , It has come to an end and You can only go left and right. Which way do you want to go : ").lower()

if answer == "left":
    answer = input("You have come to a river. Do you want to walk around or swim across? Type walk to walk around and swin to swim across: ").lower()
    
    if answer == "swim":
        print("You swim across and were drown to death")
    elif answer == "walk":
        print("You walked and walked until u died because of starvation. You lost the game.")
    else:
        print("Not a valid option. You lose")
        
elif answer == "right":
    answer = input("You come to a bridge , it looks broken , do you want to cross it or head back ? Type cross to cross the bridge and back to head back : ").lower()
    
    if answer == "back":
        print("You go back to spawn and lose the game")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to the stranger (yes/no) ? ").lower()
        
        if answer == "yes":
            print("You talk to the stranger and the stranger admired it and You WON the game!!!!")
        elif answer == "no":
            print("You ignore the stranger and you lose the game")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose.")
    
print("Thank you for playing",name)
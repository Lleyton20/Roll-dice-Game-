#Roll dice ? y/ n if a invalid choice
# if y random choice as tuple (5,2 )
# small letter or capital letter doesnt matter 
import random 

print("Welcome to rolling the dice game!!!!")
user_prompt= input("Roll dice ?").lower()# I am putting everything lower case to carter for when user enters upper case 
#user_prompt.lower()
dice_choices=[]#Idea is to return a tuple but am using a list since a tuple is immutable 
if user_prompt=="yes" :
    for i in range(2):
        ra =random.randint(1,6)
        dice_choices.append(ra)
    print(tuple(dice_choices))#Converted the list list back to a tuple

elif user_prompt=="no":
    print("Thanks for playing !!")
else:
    print("Invalid choice!!")#Case when user enters anything othere than yes or no/YES OR NO
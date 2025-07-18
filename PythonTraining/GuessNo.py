import random

number=random.randint(1,10)

while True:
   Guess=input("Guess the number between (1 to 10):")
   Guess=int(Guess)

   if Guess == number:
        print("You Win!!!")
   else:
        print("You Lose")    


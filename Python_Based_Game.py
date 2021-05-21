import random
import math

def guess_game():
	low = int(input("Enter Lower Range:- "))
	up = int(input("Enter Upper Range:- "))

	random_number = random.randint(low, up)
	chance=round(math.log(up - low))
	print("You've only " , chance , " chances to guess the integer!\n")
	temp=0
	count = 0
	while(count < chance): 
		count += 1
		guess = int(input("Guess a number:- "))

		if (random_number == guess):
			print("Congratulations!! you did it in ", count , "  Chance")
			break
		elif (random_number > guess):
			print("You guessed a number smaller than the real one!!")
		else:
			print("You guessed a number greater than the real one!!")


	if (count >= chance):
		print("\nThe number is " , random_number)
		print("\tBetter Luck Next time!!")

def alphabet_guess():
	random_number = random.randint(65,90)
	c=chr(random_number)

	chance=6
	print("You've only " , chance , " chances to guess the right Alphabet!\n")
	count = 0
	while(count < chance): 
		count += 1
		guess = str(input("Guess an Alphabet- "))

		if (c == guess):
			print("Congratulations!! you did it in ", count , "  Chance")
			break
		else:
			print("MISSED !!")


	if (count >= chance):
		print("\nThe Alphabhet is " , c)
		print("\tBetter Luck Next time!!")

def alphabet_guess2():
	random_number = random.randint(97,122)
	c=chr(random_number)

	chance=6
	print("\n\nYou've only " , chance , " chances to guess the right Alphabet!\n\n")
	count = 0
	while(count < chance): 
		count += 1
		guess = str(input("Guess an Alphabet- "))

		if (c == guess):
			print("Congratulations!! you did it in ", count , "  Chance")
			break
		else:
			print("MISSED !!")


	if (count >= chance):
		print("\nThe Alphabhet is " , c)
		print("\tBetter Luck Next time!!")


if __name__ == '__main__':
    print("\n\n**************************************************\n")
    print("Enter 1- for Playing with Numbers")
    print("Enter 2- for Playing with Capital Letter")
    print("Enter 3- for Playing with Small Letter")
    print("\n**************************************************\n\n")

    select = int(input("Enter your choice : "))

    if(select==1):
        guess_game()
    elif(select==2):
        alphabet_guess()
    elif(select==3):
        alphabet_guess2()
    else:
        print("********************************Thank You********************************")   

    print("********************************Thank You********************************")   

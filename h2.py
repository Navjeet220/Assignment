import random

def welcomeScreen():
	name=input("Your name: ")
	print("WELCOME",name,"You are going to play the HANGMAN game")
	print("Try to guess the word in minimum tries")
	print("Good luck!")
	draw_board()
	print()
	user_guess()
	print()
	
movies=["MOHABTEIN","JAB WE MET","CHAK DE INDIA","LOVE AAJ KAL","PHILAURI","HARRY POTTER","TWILIGHT","BHAUBALLI","SURYAVANSHM","CHANDRMUKHI"]
random.shuffle(movies)

secret_word=movies.pop()
correct=[]
incorrect=[]

print("debug:",secret_word)

def draw_board():
	for i in secret_word:
		if i in correct:
			print(i,end=' ')
		else:
			print('_',end=' ')
	print("\n\n")
	print("missed letters")
	for i in incorrect:
		print(i,end=' ')
	print('\n*******************************')
	
def user_guess():
	while True:
			guess=input("Guess a letter:\n ")
		if guess in correct or guess in incorrect:
			print("you already guessed that letter,guess another letter again")
		elif guess.isnumeric():
			print("please enter only alphabets not numbers,guess a letter again")
		elif len(guess)>1:
			print("enter only one letter at a time")
		elif len(guess)==0:
			print("enter your selection")
		else:
			break	
	
	if guess in secret_word:
		correct.append(guess)
	else:
		incorrect.append(guess)
	
while True:
	welcomeScreen()
	draw_board()
	user_guess()
	
	break
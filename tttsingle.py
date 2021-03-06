#tictactoe
#author callmedraken github.com/callmedraken

import random

board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
global curr

# init and draws the board
def draw():
	print(" %c | %c | %c " % (board[0],board[1],board[2]))    
	print("___|___|___")    
	print(" %c | %c | %c " % (board[3],board[4],board[5]))    
	print("___|___|___")    
	print(" %c | %c | %c " % (board[6],board[7],board[8]))    
	print("   |   |   ")   
	
# choose the player that goes first based on a random seed
# @param first : the number player 1 chose
# @param second : the number player 2 chose
# @param seed : the random seed
def selectPlayer(first, second, seed):
	weightA = seed - first
	weightB = seed - second
	weightA = abs(weightA)
	weightB = abs(weightB)
	if (weightA > weightB):
		print("Computer goes first.")
		return 2
	else:
		print("You go first.")
		return 1

def checkMove(num):
	# return false if the board at pos is empty
	if board[num] == '*':
		return True
	else:
		return False

# checks if the game is won
def checkStatus():
	# top row
	if (board[0] == board[1] and board[1] == board[2] and board[0] != '*'):
		return True
	# mid row
	elif (board[3] == board[4] and board[4] == board[5] and board[3] != '*'):
		return True
	# bot row
	elif (board[6] == board[7] and board[7] == board[8] and board[6] != '*'):
		return True
	# first column
	elif (board[0] == board[3] and board[3] == board[6] and board[0] != '*'):
		return True
	# second column
	elif (board[1] == board[4] and board[4] == board[7] and board[1] != '*'):
		return True
	# third column
	elif (board[2] == board[5] and board[5] == board[8] and board[2] != '*'):
		return True
	# right diagonal
	elif (board[0] == board[4] and board[4] == board[8] and board[0] != '*'):
		return True
	# left diagonal
	elif (board[2] == board[4] and board[4] == board[6] and board[2] != '*'):
		return True

def botCheckMove(bMove):
	# top row right to left
	if (board[0] == board[1] and board[0] == 'X'):
		return 3
	# top row left to right
	if (board[2] == board[1] and board[2] == 'X'):
		return 1
	# mid row right to left
	elif (board[3] == board[4] and board[3] == 'X'):
		return 6
	# mid row left to right
	elif (board[5] == board[4] and board[5] == 'X'):
		return 4
	# bot row right to left
	elif (board[6] == board[7] and board[6] == 'X'):
		return 9
	# bot row left to right
	elif (board[8] == board[7] and board[8] == 'X'):
		return 7
	# first column up to down
	elif (board[0] == board[3] and board[0] == 'X'):
		return 7
	# first column down to up
	elif (board[6] == board[3] and board[6] == 'X'):
		return 1
	# second column up to down
	elif (board[1] == board[4] and board[1] == 'X'):
		return 8
	# second column down to up
	elif (board[7] == board[4] and board[7] == 'X'):
		return 2
	# third column up to down
	elif (board[2] == board[5] and board[2] == 'X'):
		return 9
	# third column down to up
	elif (board[8] == board[5] and board[8] == 'X'):
		return 3
	# right diagonal down
	elif (board[0] == board[4] and board[0] == 'X'):
		return 9
	# left diagonal down
	elif (board[2] == board[4] and board[2] == 'X'):
		return 7
	# right diagonal up
	elif (board[8] == board[4] and board[8] == 'X'):
		return 1
	# left diagonal up
	elif (board[6] == board[4] and board[6] == 'X'):
		return 3
	else:
		return bMove
		
def playGame():
	counter = 0
	win = 0
	global curr
	while win == 0 and counter < 9:
		if curr == 1:
			aMove = int(input("Select a move(1-9): "))
			aMove = aMove - 1
			while checkMove(aMove) == False:
				print("Square already selected...")
				aMove = int(input("Select a move(1-9): "))
				aMove = aMove - 1
			board[aMove] = 'X'
			moves.remove(aMove + 1)
			draw()
			if checkStatus() == True:
				print("Congratulations, you win!")
				win = 1
			curr = 2
			counter += 1
		else:
			print("Computer move...")
			bMove = random.choice(moves)
			bMove = botCheckMove(bMove)
			if checkMove(bMove - 1) == False:
				bMove = random.choice(moves)
			moves.remove(bMove)
			bMove = bMove - 1
			board[bMove] = 'O'
			draw()
			if checkStatus() == True:
				print("Sorry, Computer wins!")
				win = 2
			curr = 1
			counter += 1
	if win == 0:
		print("No one won :(.")
		
def main():
	print("Welcome to Tic Tac Toe")
	print("You are \"X\" and player 2 is \"O\"")
	print("Deciding who makes the first move..")
	while True:
		A = int(input("Please choose a number between 0 and 100: "))
		if (-1) < A < 101:
			break
		else:
			print("out of bound selection.")
	B = random.randint(0, 100)
	print("Computer randomized %d." % B)
	seed = random.randint(0, 100)
	print(seed)
	global curr
	curr = selectPlayer(A, B, seed)
	draw()
	playGame()

main()

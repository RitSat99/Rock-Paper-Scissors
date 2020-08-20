import random

moves=['Rock','Paper','Scissors']
plwin=0
aiwin=0


print('Welcome to ENDLESS Rock Paper Scissors!!')
print("You can enter 'Quit' to quit the game :P")

while True:

	playermove=input("READY? Play your move!! Rock, Paper or Scissors? ")
	if playermove.lower()[0]=='r':
		playermove='Rock'
		print(f'Your Move: {playermove}')
	if playermove.lower()[0]=='p':
		playermove='Paper'
		print(f'Your Move: {playermove}')
	if playermove.lower()[0]=='s':
		playermove='Scissors'
		print(f'Your Move: {playermove}')
	if playermove.lower()[0]=='q':
		print('Thanks for playing, This was brought to you by Ritwik Satpathy')
		break

	

	ai_choice=random.choice(moves)
	print(f'Computer plays: {ai_choice}')

	if playermove==ai_choice:
		print("It's a TIE")
	if playermove=='Rock' and ai_choice=='Paper':
		print("SIGH!! you LOSE")
		aiwin+=1
	if playermove=='Rock' and ai_choice=='Scissors':
		print("YAY!! it's a WIN")
		plwin+=1
	if playermove=='Paper' and ai_choice=='Rock':
		print("YAY!! it's a WIN")
		plwin+=1
	if playermove=='Paper' and ai_choice=='Scissors':
		print("SIGH!! you LOSE")
		aiwin+=1
	if playermove=='Scissors' and ai_choice=='Rock':
		print("SIGH!! you LOSE")
		aiwin+=1
	if playermove=='Scissors' and ai_choice=='Paper':
		print("YAY!! it's a WIN")
		plwin+=1

	print(f'You: {plwin} vs Computer: {aiwin}')


# Ritwik Satpathy
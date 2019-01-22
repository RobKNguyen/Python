'''
Main program for Black Jack Milestone Project.
'''
from SubModule import BlackJack_Implementation

# TESTER FOR LINKING Implementation module.
#BlackJack_Implementation.link_tester()

def prompt_user():
	response=input('Would you like to play again?\n(yes/y to play or no/n to not)\n').lower()
	if(response=='y' or 'yes'):
		return True
	elif(response=='n' or response=='no'):
		return False
	else:
		valid_response=prompt_user()
		return valid_response

def hit_or_naw():
	hit_or_naw=input('Would you like to hit or naw?\nD to hit. A to stay.\n').lower()
	if (hit_or_naw=='d'):
		return True
	elif(hit_or_naw=='a'):
		return False
	else:
		correct_answer=hit_or_naw()
		return correct_answer

'''
hearts = BlackJack_Implementation.Cards('hearts','red')
spades = BlackJack_Implementation.Cards('spades','black')
diamonds = BlackJack_Implementation.Cards('diamonds','red')
clubs = BlackJack_Implementation.Cards('clubs','black')
'''
player_win_count=0
cpu_win_count=0
game_over=False
new_game = BlackJack_Implementation.Game()
new_game.deal_first_hand()
print('Your hand is: {}'.format(new_game.player_hand))
print('Your opponents hand is: {}'.format(new_game.cpu_hand))
while game_over==False:
	hit_or_miss=hit_or_naw()
	if(hit_or_miss):
		new_game.hit_me()
		print('Total: {}'.format(new_game.player_total))
		print('Total: {}'.format(new_game.cpu_hand))
		if(new_game.player_total>21):
			print('BUSTED')
			game_over=True
		continue
	else:
		print('Player chooses to stay.')
		print('Results:')
		print('Your Total: {}'.format(new_game.player_total))
		print('CPU Total: {}'.format(new_game.cpu_total))
		if(new_game.cpu_total>21):
			print('Cpu busted. You win.')
			player_win_count += 1
			game_over=True
		elif(new_game.player_total > new_game.cpu_total):
			print('You won!')
			player_win_count+=1
			game_over=True
		elif(new_game.player_total < new_game.cpu_total):
			print('You lost!')
			cpu_win_count+=1
			game_over=True


'''
print('Your hand is: {}'.format(new_game.player_hand))
print('Your opponents hand is: {}'.format(new_game.cpu_hand))
hit_or_naw()
print('Your total is: {}'.format(new_game.player_total))
print('Opponents total is: {}'.format(new_game.cpu_total))
'''

#print(spades)
#print(spades.card_selection)
#user_response = prompt_user()

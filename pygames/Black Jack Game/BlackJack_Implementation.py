'''
Implementation file for Black Jack Class.
'''
'''
def link_tester():
	print('BlackJack_Implementation is linked.')
'''
from random import randint
import random

'''
class Cards():
	card_selection={'1':1,'2':2,'3':3,'4':4,'5':5,
	'6':6,'7':7,'8':8,'9':9,'10':10,'JACK':10,
	'QUEEN':10,'KING':10,'A':11}

	card_selection_list=['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a']

	card_dict_list={'hearts':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a'],'spades':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a'],'diamonds':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a'],'clubs':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a']}
	

	card_used={'1':False,'2':False,'3':False,'4':False,'5':False,
	'6':False,'7':False,'8':False,'9':False,'10':False,'JACK':False,
	'QUEEN':False,'KING':False,'A':False}

	def __init__(self,card_name,card_color):
		self.card_name=card_name
		self.card_color=card_color

	def __str__(self):
		return self.card_name
'''

class Game():

	card_dict_list={'hearts':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a'],'spades':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a'],'diamonds':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a'],'clubs':['1','2','3','4','5',
	'6','7','8','9','10','jack','queen','king','a']}

	player_hand=[]
	cpu_hand=[]
	player_total=0
	cpu_total=0

	def __init__(self):
		print('Initializing game.')

	def deal_first_hand(self):
		# DEALS PLAYER HAND.
		for _ in range(0,2):

			rando=randint(1,4)
			card_type=''
			if (rando==1):
				#print('card_type is hearts!')
				card_type='hearts'
			elif (rando==2):
				#print('card_type is spades!')
				card_type='spades'
			elif (rando==3):
				#print('card_type is diamonds!')
				card_type='diamonds'
			elif (rando==4):
				#print('card_type is clubs!')
				card_type='clubs'

			card=random.choice(Game.card_dict_list[card_type])
			#print('Drawing card: {}'.format(card))
			Game.player_hand.append(card)
			Game.card_dict_list[card_type].remove(card)
			#print(card)
			#print(Game.card_dict_list[card_type])
		# DEALS CPU HAND.
		for _ in range(0,2):

			rando=randint(1,4)
			card_type=''
			if (rando==1):
				#print('card_type is hearts!')
				card_type='hearts'
			elif (rando==2):
				#print('card_type is spades!')
				card_type='spades'
			elif (rando==3):
				#print('card_type is diamonds!')
				card_type='diamonds'
			elif (rando==4):
				#print('card_type is clubs!')
				card_type='clubs'

			card=random.choice(Game.card_dict_list[card_type])
			#print('Drawing card: {}'.format(card))
			Game.cpu_hand.append(card)
			Game.card_dict_list[card_type].remove(card)
			#print(card)
			#print(Game.card_dict_list[card_type])
		Game.player_total=0
		for cards in Game.player_hand:
			if cards=='a':
				cards=11
			elif cards=='jack' or cards=='queen' or cards=='king':
				cards=10
			Game.player_total=Game.player_total+int(cards)
		if Game.player_total>21 and 'a' in Game.player_hand:
			Game.player_total=Game.player_total-10

		Game.cpu_total=0
		for cards in Game.cpu_hand:
			if cards=='a':
				cards=11
			elif cards=='jack' or cards=='queen' or cards=='king':
				cards=10
			Game.cpu_total=Game.cpu_total+int(cards)
		if Game.cpu_total>21 and 'a' in Game.cpu_hand:
			Game.cpu_total=Game.cpu_total-10

	def hit_me(self):
		rando=randint(1,4)
		card_type=''
		if (rando==1):
			#print('card_type is hearts!')
			card_type='hearts'
		elif (rando==2):
			#print('card_type is spades!')
			card_type='spades'
		elif (rando==3):
			#print('card_type is diamonds!')
			card_type='diamonds'
		elif (rando==4):
			#print('card_type is clubs!')
			card_type='clubs'

		card=random.choice(Game.card_dict_list[card_type])
		#print('Drawing card: {}'.format(card))
		Game.player_hand.append(card)
		Game.card_dict_list[card_type].remove(card)
		print('YOU DRAW: {}'.format(card))
		#print(card)
		#print(Game.card_dict_list[card_type])
		Game.player_total=0
		for cards in Game.player_hand:
			if cards=='a':
				cards=11
			elif cards=='jack' or cards=='queen' or cards=='king':
				cards=10
			Game.player_total=Game.player_total+int(cards)
		if Game.player_total>21 and 'a' in Game.player_hand:
			Game.player_total=Game.player_total-10

		temp_cpu_total=0
		for cards in Game.cpu_hand:
			if cards=='a':
				cards=11
			elif cards=='jack' or cards=='queen' or cards=='king':
				cards=10
			temp_cpu_total=temp_cpu_total+int(cards)

		if temp_cpu_total < 16:
			rando=randint(1,4)
			card_type=''
			if (rando==1):
				print('card_type is hearts!')
				card_type='hearts'
			elif (rando==2):
				print('card_type is spades!')
				card_type='spades'
			elif (rando==3):
				print('card_type is diamonds!')
				card_type='diamonds'
			elif (rando==4):
				print('card_type is clubs!')
				card_type='clubs'

			card=random.choice(Game.card_dict_list[card_type])
			#print('Drawing card: {}'.format(card))
			Game.cpu_hand.append(card)
			Game.card_dict_list[card_type].remove(card)
			print('CPU DRAWS: {}'.format(card))
			#print(Game.card_dict_list[card_type])
		Game.cpu_total=0
		for cards in Game.cpu_hand:
			if cards=='a':
				cards=11
			elif cards=='jack' or cards=='queen' or cards=='king':
				cards=10
			Game.cpu_total=Game.cpu_total+int(cards)
		if Game.cpu_total>21 and 'a' in Game.cpu_hand:
			Game.cpu_total=Game.cpu_total-10

def user_prompter():
    answer=input("Hello, would you like to be X's or O's? (Enter X or O)\n").lower()
    player_setup={}
    if answer=='x':
        player_setup={'Player1':'X','Player2':'O'}
    elif answer=='o':
        player_setup={'Player1':'O','Player2':'X'}
    else:
        player_setup=user_prompter()
    return player_setup

def game_starter():
    answer=input("Would you like to initiate game? (yes or no, or you can type y or n)\n").lower()
    if (answer=='y' or answer=='yes'):
        return True
    elif (answer=='no' or answer== 'n'):
        return False
    else:
        will_it_start = game_starter()
        return will_it_start

def player_move():
    choice=input("Enter number between 1 and 9 (Enter 1 - 9 on keyboard).\n")
    if(choice=='1' or choice=='2' or choice=='3' or choice=='4' or choice=='5' or choice=='6' or choice=='7' or choice=='8' or choice=='9'):
        return choice
    else:
        choice=player_move()
        return choice


def player_turn_setup():
    answer=input("Do you want to go first? (y or n)\n").lower()
    if (answer=='y' or answer=='yes'):
        return True
    elif (answer=='no' or answer== 'n'):
        return False
    else:
        player_turn=player_turn_setup()
        return player_turn

def check_if_gameover(game_mark, game_spots):
    #print('GAME MARKER FUNCTION: ' + game_mark['1'])
    #print(game_mark['1'] + ' ' + game_mark['2'] + game_mark['3'] + ' ' + game_mark['4'] + game_mark['5'] + ' ' + game_mark['6'] + game_mark['7'] + ' ' + game_mark['8'] + game_mark['9'])
    if((game_mark['1']==game_mark['2']) and (game_mark['2']==game_mark['3'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif((game_mark['4']==game_mark['5']) and (game_mark['5']==game_mark['6'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif((game_mark['7']==game_mark['8']) and (game_mark['8']==game_mark['9'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif((game_mark['1']==game_mark['4']) and (game_mark['4']==game_mark['7'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif((game_mark['2']==game_mark['5']) and (game_mark['5']==game_mark['8'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif((game_mark['3']==game_mark['6']) and (game_mark['6']==game_mark['9'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif((game_mark['1']==game_mark['5']) and (game_mark['5']==game_mark['9'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif((game_mark['3']==game_mark['5']) and (game_mark['5']==game_mark['7'])):
        print('Winner winner, NOW GO GET SOME GAINZ')
        return True
    elif(game_spots['1']==True and game_spots['2']==True and game_spots['3']==True and game_spots['4']==True and game_spots['5']==True and game_spots['6']==True and game_spots['7']==True and game_spots['8']==True and game_spots['9']==True):
        print('RAN OUT OF SPACE.')
        return True
    else:
        return False

def play_again():
    answer=input("Play again? (yes/y or no/n)\n").lower()
    if (answer=='y' or answer=='yes'):
        return True
    elif (answer=='no' or answer== 'n'):
        return False
    else:
        play_once_again=play_again()
        return play_once_again



user_setup=user_prompter()
user_startup=game_starter()
if(user_startup):
    game_end=False
    play_again=True
    while(play_again==True):
        game_board={'Row 1':'   |   |   \n   |   |   \n   |   |   ','HL1':'-----------','Row 2':'   |   |   \n   |   |   \n   |   |   ','HL2':'-----------','Row 3':'   |   |   \n   |   |   \n   |   |   '}
        game_spot_taken={'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False}
        game_marker={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}
        game_board_list=[game_board['Row 1'],game_board['HL1'],game_board['Row 2'],game_board['HL2'],game_board['Row 3']]
        for key,value in game_board.items():
            print(value)
    
        #play_again=False
        player1_turn = player_turn_setup()
        while(game_end!=True):
            if(player1_turn):
                print('Player 1: ')
                while(player1_turn):
                    choice=str(player_move())   #Retreives player's choice from 1 - 9

                    print('Player choice: '+choice)
                    if(choice=='1' and game_spot_taken['1']==False):
                        game_board['Row 3'] = game_board['Row 3'][0:13:]+user_setup['Player1']+game_board['Row 3'][14::]
                        game_board_list[4] = game_board['Row 3']
                        game_spot_taken['1']=True
                        game_marker['1']='X'
                    elif(choice=='2' and game_spot_taken['2']==False):
                        game_board['Row 3'] = game_board['Row 3'][0:17:]+user_setup['Player1']+game_board['Row 3'][18::]
                        game_board_list[4] = game_board['Row 3']
                        game_spot_taken['2']=True
                        game_marker['2']='X'
                    elif(choice=='3' and game_spot_taken['3']==False):
                        game_board['Row 3'] = game_board['Row 3'][0:21:]+user_setup['Player1']+game_board['Row 3'][22::]
                        game_board_list[4] = game_board['Row 3']
                        game_spot_taken['3']=True
                        game_marker['3']='X'
                    elif(choice=='4' and game_spot_taken['4']==False):
                        game_board['Row 2'] = game_board['Row 2'][0:13:]+user_setup['Player1']+game_board['Row 2'][14::]
                        game_board_list[2] = game_board['Row 2']
                        game_spot_taken['4']=True
                        game_marker['4']='X'
                    elif(choice=='5' and game_spot_taken['5']==False):
                        game_board['Row 2'] = game_board['Row 2'][0:17:]+user_setup['Player1']+game_board['Row 2'][18::]
                        game_board_list[2] = game_board['Row 2']
                        game_spot_taken['5']=True
                        game_marker['5']='X'
                    elif(choice=='6' and game_spot_taken['6']==False):
                        game_board['Row 2'] = game_board['Row 2'][0:21:]+user_setup['Player1']+game_board['Row 2'][22::]
                        game_board_list[2] = game_board['Row 2']
                        game_spot_taken['6']=True
                        game_marker['6']='X'
                    elif(choice=='7' and game_spot_taken['7']==False):
                        game_board['Row 1'] = game_board['Row 1'][0:13:]+user_setup['Player1']+game_board['Row 1'][14::]
                        game_board_list[0] = game_board['Row 1']
                        game_spot_taken['7']=True
                        game_marker['7']='X'
                    elif(choice=='8'and game_spot_taken['8']==False):
                        game_board['Row 1'] = game_board['Row 1'][0:17:]+user_setup['Player1']+game_board['Row 1'][18::]
                        game_board_list[0] = game_board['Row 1']
                        game_spot_taken['8']=True
                        game_marker['8']='X'
                    elif(choice=='9' and game_spot_taken['9']==False):
                        game_board['Row 1'] = game_board['Row 1'][0:21:]+user_setup['Player1']+game_board['Row 1'][22::]
                        game_board_list[0] = game_board['Row 1']
                        game_spot_taken['9']=True
                        game_marker['9']='X'
                    else:
                        print('Spot is already taken.')
                        continue
                    for items in game_board_list:
                        print(items)
                    player1_turn=False
                    checker=check_if_gameover(game_marker, game_spot_taken)
                    #print(checker)
                    game_end=checker

            elif(player1_turn==False):
                print('Player 2: ')
                choice=str(player_move())
                print('Player 2 Enters: '+choice)
                if(choice=='1' and game_spot_taken['1']==False):
                    game_board['Row 3'] = game_board['Row 3'][0:13:]+user_setup['Player2']+game_board['Row 3'][14::]
                    game_board_list[4] = game_board['Row 3']
                    game_spot_taken['1']=True
                    game_marker['1']='O'
                elif(choice=='2' and game_spot_taken['2']==False):
                    game_board['Row 3'] = game_board['Row 3'][0:17:]+user_setup['Player2']+game_board['Row 3'][18::]
                    game_board_list[4] = game_board['Row 3']
                    game_spot_taken['2']=True
                    game_marker['2']='O'
                elif(choice=='3' and game_spot_taken['3']==False):
                    game_board['Row 3'] = game_board['Row 3'][0:21:]+user_setup['Player2']+game_board['Row 3'][22::]
                    game_board_list[4] = game_board['Row 3']
                    game_spot_taken['3']=True
                    game_marker['3']='O'
                elif(choice=='4' and game_spot_taken['4']==False):
                    game_board['Row 2'] = game_board['Row 2'][0:13:]+user_setup['Player2']+game_board['Row 2'][14::]
                    game_board_list[2] = game_board['Row 2']
                    game_spot_taken['4']=True
                    game_marker['4']='O'
                elif(choice=='5' and game_spot_taken['5']==False):
                    game_board['Row 2'] = game_board['Row 2'][0:17:]+user_setup['Player2']+game_board['Row 2'][18::]
                    game_board_list[2] = game_board['Row 2']
                    game_spot_taken['5']=True
                    game_marker['5']='O'
                elif(choice=='6' and game_spot_taken['6']==False):
                    game_board['Row 2'] = game_board['Row 2'][0:21:]+user_setup['Player2']+game_board['Row 2'][22::]
                    game_board_list[2] = game_board['Row 2']
                    game_spot_taken['6']=True
                    game_marker['6']='O'
                elif(choice=='7' and game_spot_taken['7']==False):
                    game_board['Row 1'] = game_board['Row 1'][0:13:]+user_setup['Player2']+game_board['Row 1'][14::]
                    game_board_list[0] = game_board['Row 1']
                    game_spot_taken['7']=True
                    game_marker['7']='O'
                elif(choice=='8' and game_spot_taken['8']==False):
                    game_board['Row 1'] = game_board['Row 1'][0:17:]+user_setup['Player2']+game_board['Row 1'][18::]
                    game_board_list[0] = game_board['Row 1']
                    game_spot_taken['8']=True
                    game_marker['8']='O'
                elif(choice=='9' and game_spot_taken['9']==False):
                    game_board['Row 1'] = game_board['Row 1'][0:21:]+user_setup['Player2']+game_board['Row 1'][22::]
                    game_board_list[0] = game_board['Row 1']
                    game_spot_taken['9']=True
                    game_marker['9']='O'
                else:
                    print('Spot is already taken.')
                    continue

                for items in game_board_list:
                    print(items)
                player1_turn=True
                checker=check_if_gameover(game_marker, game_spot_taken)
                #print(checker)
                game_end=checker

        #stay_in_loop=True
        #while(stay_in_loop):
        user_response=input('Play Again? (press anything to start new game. (Enter n to end): \n').lower()
        if(user_response!='n'):
            #stay_in_loop=False
            play_again=True
        elif(user_response=='n' or user_response=='no'):
            #stay_in_loop=False
            play_again=False

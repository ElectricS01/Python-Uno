import random
import textwrap

color = ['red', 'green', 'blue', 'yellow']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'skip', 'reverse', '+2']
deal = 5
player_deck = []
enemy_deck = []
top_card = 'empty'

cc = []
turn = 'player'
deck = ['wild', 'wild', 'wild', 'wild', '+4', '+4', '+4', '+4', 'yellow 0', 'yellow 1', 'yellow 2', 'yellow 3',
        'yellow 4', 'yellow 5', 'yellow 6', 'yellow 7', 'yellow 8', 'yellow 9', 'yellow 1', 'yellow 2', 'yellow 3',
        'yellow 4', 'yellow 5', 'yellow 6', 'yellow 7', 'yellow 8', 'yellow 9', 'red 0', 'red 1', 'red 2', 'red 3',
        'red 4', 'red 5', 'red 6', 'red 7', 'red 8', 'red 9', 'red 1', 'red 2', 'red 3', 'red 4', 'red 5', 'red 6',
        'red 7', 'red 8', 'red 9', 'blue 0', 'blue 1', 'blue 2', 'blue 3', 'blue 4', 'blue 5', 'blue 6', 'blue 7',
        'blue 8', 'blue 9', 'blue 1', 'blue 2', 'blue 3', 'blue 4', 'blue 5', 'blue 6', 'blue 7', 'blue 8', 'blue 9',
        'green 0', 'green 1', 'green 2', 'green 3', 'green 4', 'green 5', 'green 6', 'green 7', 'green 8', 'green 9',
        'green 1', 'green 2', 'green 3', 'green 4', 'green 5', 'green 6', 'green 7', 'green 8', 'green 9',
        'yellow reverse', 'yellow reverse', 'red reverse', 'red reverse', 'blue reverse', 'blue reverse',
        'green reverse', 'green reverse', 'yellow skip', 'yellow skip', 'red skip', 'red skip', 'blue skip',
        'blue skip', 'green skip', 'green skip', 'yellow +2', 'yellow +2', 'red +2', 'red +2', 'blue +2', 'blue +2',
        'green +2', 'green +2']

random.shuffle(deck)

print("Made by ElectricS01")
# Do Not Redistribute without permission

input('Ready?')

while deal > 0:
    player = deck[0]
    deck.remove(player)
    enemy = deck[0]
    deck.remove(enemy)
    deal -= 1
    player_deck.append(player)
    enemy_deck.append(enemy)

print(f'Your deck is:{player_deck}')
print()
while 'empty' in top_card:
    if '+4' not in deck[0]:
        if 'wild' not in deck[0]:
            top_card = deck[0]
            deck.remove(top_card)
        else:
            deck.remove(deck[0])
    else:
        deck.remove(deck[0])

while 0 < 1:
    while turn == 'player':
        action_col = ['a']
        top_card_col = ['b']
        action_num = ['c']
        top_card_num = ['d']
        print(f'The top card is {top_card}, Your deck: {player_deck}.')
        print()
        action = str.casefold(input("Play a card or \"Draw\" a card "))
        if action in player_deck or 'draw' in action:
            print()

            if 'wild' in action and 'wild' in player_deck:
                cc = str.casefold(input('Select colour(Red/Green/Blue/Yellow) '))
                print()
                if cc in color:
                    top_card = f'{cc}_wild'
                    turn = 'enemy'
                    player_deck.remove('wild')

            if '+4' in action and '+4' in player_deck:
                cc = str.casefold(input('Select colour(Red/Green/Blue/Yellow) '))
                print()
                if cc in color:
                    top_card = f'{cc}_+4'
                    repeat = 4
                    while repeat > 0:
                        if len(deck) > 0:
                            enemy_deck.append(deck[0])
                            deck.remove(deck[0])
                        repeat -= 1
                    player_deck.remove('+4')

            if 'draw' in action:
                if len(deck) > 0:
                    player_deck.append(deck[0])
                    remove = deck[0]
                    deck.remove(remove)
                    turn = 'enemy'
                else:
                    print('the deck is empty')

            if 'wild' not in action:
                if '+4' not in action:
                    if 'draw' not in action:

                        if ('draw' or ('+4' or 'wild')) not in action:
                            if 'blue' in action:
                                action_col = 'blue '
                            if 'yellow' in action:
                                action_col = 'yellow '
                            if 'green' in action:
                                action_col = 'green '
                            if 'red' in action:
                                action_col = 'red '

                            if 'blue' in top_card:
                                top_card_col = 'blue '
                            if 'yellow' in top_card:
                                top_card_col = 'yellow '
                            if 'green' in top_card:
                                top_card_col = 'green '
                            if 'red' in top_card:
                                top_card_col = 'red '

                            if '0' in action:
                                action_num = '0'
                            if '1' in action:
                                action_num = '1'
                            if '2' in action:
                                action_num = '2'
                            if '3' in action:
                                action_num = '3'
                            if ' 4' in action:
                                action_num = '4'
                            if '5' in action:
                                action_num = '5'
                            if '6' in action:
                                action_num = '6'
                            if '7' in action:
                                action_num = '7'
                            if '8' in action:
                                action_num = '8'
                            if '9' in action:
                                action_num = '9'
                            if 'skip' in action:
                                action_num = 'skip'
                            if 'reverse' in action:
                                action_num = 'reverse'
                            if '+2' in action:
                                action_num = '+2'

                            if '0' in top_card:
                                top_card_num = '0'
                            if '1' in top_card:
                                top_card_num = '1'
                            if ' 2' in top_card:
                                top_card_num = '2'
                            if '3' in top_card:
                                top_card_num = '3'
                            if '4' in top_card:
                                top_card_num = '4'
                            if '5' in top_card:
                                top_card_num = '5'
                            if '6' in top_card:
                                top_card_num = '6'
                            if '7' in top_card:
                                top_card_num = '7'
                            if '8' in top_card:
                                top_card_num = '8'
                            if '9' in top_card:
                                top_card_num = '9'
                            if 'skip' in top_card:
                                top_card_num = 'skip'
                            if 'reverse' in top_card:
                                top_card_num = 'reverse'
                            if '+2' in top_card:
                                top_card_num = '+2'

                            if action_col == top_card_col or action_num == top_card_num:
                                if action in player_deck:
                                    player_deck.remove(action)
                                    top_card = action
                                    if 'skip' not in action:
                                        if 'reverse' not in action:
                                            if '+2' not in action:
                                                turn = 'enemy'
                                    if '+2' in action:
                                        repeat = 2
                                        while repeat > 0:
                                            if len(deck) > 0:
                                                enemy_deck.append(deck[0])
                                                deck.remove(deck[0])
                                            repeat -= 1

                            else:
                                if ('+4' or 'wild') not in action:
                                    print(action)
                                    print("This card can't be played")
        else:
            print("This card can't be played")

    print(deck)

    while turn == 'enemy':

        check = len(enemy_deck)
        check -= 1

        while check > -1:
            if 'blue' in action:
                action_col = 'blue'
            if 'yellow' in action:
                action_col = 'yellow'
            if 'green' in action:
                action_col = 'green'
            if 'red' in action:
                action_col = 'red'

            if 'blue' in top_card:
                top_card_col = 'blue'
            if 'yellow' in top_card:
                top_card_col = 'yellow'
            if 'green' in top_card:
                top_card_col = 'green'
            if 'red' in top_card:
                top_card_col = 'red'

            if '0' in action:
                action_num = '0'
            if '1' in action:
                action_num = '1'
            if ' 2' in action:
                action_num = '2'
            if '3' in action:
                action_num = '3'
            if '4' in action:
                action_num = '4'
            if '5' in action:
                action_num = '5'
            if '6' in action:
                action_num = '6'
            if '7' in action:
                action_num = '7'
            if '8' in action:
                action_num = '8'
            if '9' in action:
                action_num = '9'
            if 'skip' in action:
                action_num = 'skip'
            if 'reverse' in action:
                action_num = 'reverse'
            if '+2' in action:
                action_num = '+2'

            if '0' in top_card:
                top_card_num = '0'
            if '1' in top_card:
                top_card_num = '1'
            if ' 2' in top_card:
                top_card_num = '2'
            if '3' in top_card:
                top_card_num = '3'
            if '4' in top_card:
                top_card_num = '4'
            if '5' in top_card:
                top_card_num = '5'
            if '6' in top_card:
                top_card_num = '6'
            if '7' in top_card:
                top_card_num = '7'
            if '8' in top_card:
                top_card_num = '8'
            if '9' in top_card:
                top_card_num = '9'
            if 'skip' in top_card:
                top_card_num = 'skip'
            if 'reverse' in top_card:
                top_card_num = 'reverse'
            if '+2' in top_card:
                top_card_num = '+2'

            if action_col == top_card_col or action_num == top_card_num:
                action = random.choice(enemy_deck)
            else:
                if check == 0:
                    action = 'draw'
                else:
                    print(enemy_deck)
                    check -= 1

            print(action)

            if 'draw' in action:
                if len(deck) > 0:
                    enemy_deck.append(deck[0])
                    remove = deck[0]
                    deck.remove(remove)
                    turn = 'player'
                else:
                    print('the deck is empty 2')
                    print(deck)

            if action_col == top_card_col or action_num == top_card_num:
                enemy_deck.remove(action)
                top_card = action
                turn = 'player'
                print(action_col, top_card_col, action_num, top_card_num)

    if player_deck == []:
        print('You Win!!')
        break

    if enemy_deck == []:
        print('You Lose:(')
        break

    if deck == []:
        if enemy_deck > player_deck:
            print('You Win!!')
            break
        else:
            print('You Lose:(')
            break

input()
wrapper = textwrap.TextWrapper(width=50)

word_list = wrapper.wrap(text=deck)

for element in word_list:
    print(element)
print()
print(top_card)
print(player_deck)
print(enemy_deck)

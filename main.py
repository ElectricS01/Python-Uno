import random
import textwrap

color = ['red', 'green', 'blue', 'yellow']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
deal = 5
playerdeck = []
enemydeck = []

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

print("Made by ElectricS01(Thomas B)")
# Do Not Redistribute without permission

input('Ready?')

while deal > 0:
    player = deck[0]
    deck.remove(player)
    enemy = deck[0]
    deck.remove(enemy)
    deal -= 1
    playerdeck.append(player)
    enemydeck.append(enemy)

print(f'Your deck is:{playerdeck}')
print()

topcard = deck[0]
deck.remove(topcard)

while 0 < 1:
    while turn == 'player':
        action_col = ['a']
        topcard_col = ['b']
        action_num = ['c']
        topcard_num = ['d']
        print(f'The top card is {topcard}, Your deck: {playerdeck}.')
        print()
        action = str.casefold(input("Play a card or \"Draw\" a card "))
        if action in playerdeck or 'draw' in action:
            print()

            if 'wild' in action and 'wild' in playerdeck:
                cc = str.casefold(input('Select colour(Red/Green/Blue/Yellow) '))
                if cc in color:
                    topcard = f'{cc}_wild'
                    turn = 'enemy'
                    playerdeck.remove('wild')

            if '+4' in action and '+4' in playerdeck:
                cc = str.casefold(input('Select colour(Red/Green/Blue/Yellow) '))
                if cc in color:
                    topcard = f'{cc}_+4'
                    repeat = 4
                    while repeat > 0:
                        if len(deck) > 0:
                            enemydeck.append(deck[0])
                            deck.remove(deck[0])
                        repeat -= 1
                    playerdeck.remove('+4')

            if 'draw' in action:
                if len(deck) > 0:
                    playerdeck.append(deck[0])
                    remove = deck[0]
                    deck.remove(remove)
                    turn = 'enemy'
                else:
                    print('the deck is empety')

            if ('draw' or ('+4' or 'wild')) not in action:
                if 'blue' in action:
                    action_col = 'blue '
                if 'yellow' in action:
                    action_col = 'yellow '
                if 'green' in action:
                    action_col = 'green '
                if 'red' in action:
                    action_col = 'red '

                if 'blue' in topcard:
                    topcard_col = 'blue '
                if 'yellow' in topcard:
                    topcard_col = 'yellow '
                if 'green' in topcard:
                    topcard_col = 'green '
                if 'red' in topcard:
                    topcard_col = 'red '

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

                if '0' in topcard:
                    topcard_num = '0'
                if '1' in topcard:
                    topcard_num = '1'
                if ' 2' in topcard:
                    topcard_num = '2'
                if '3' in topcard:
                    topcard_num = '3'
                if '4' in topcard:
                    topcard_num = '4'
                if '5' in topcard:
                    topcard_num = '5'
                if '6' in topcard:
                    topcard_num = '6'
                if '7' in topcard:
                    topcard_num = '7'
                if '8' in topcard:
                    topcard_num = '8'
                if '9' in topcard:
                    topcard_num = '9'
                if 'skip' in topcard:
                    topcard_num = 'skip'
                if 'reverse' in topcard:
                    topcard_num = 'reverse'
                if '+2' in topcard:
                    topcard_num = '+2'

                if action_col == topcard_col or action_num == topcard_num:
                    if action in playerdeck:
                        playerdeck.remove(action)
                        topcard = action
                        if ('+2' or ('skip' or 'reverse')) not in action:
                            turn = 'enemy'
                        if '+2' in action:
                            repeat = 2
                            while repeat > 0:
                                if len(deck) > 0:
                                    enemydeck.append(deck[0])
                                    deck.remove(deck[0])
                                repeat -= 1
                    print(action_col, topcard_col, action_num, topcard_num)

                else:
                    if ('+4' or 'wild') not in action:
                        print(action)
                        print("This card can't be played")
        else:
            print("This card can't be played")

    while turn == 'enemy':
        range = len(enemydeck)
        action_random = [random.choice(enemydeck), 'draw']

        action = random.choice(action_random)

        print(action)

        if 'draw' in action:
            if len(deck) > 0:
                enemydeck.append(deck[0])
                remove = deck[0]
                deck.remove(remove)
                turn = 'player'
            else:
                print('the deck is empety')
        else:
            if 'blue' in action:
                action_col = 'blue'
            if 'yellow' in action:
                action_col = 'yellow'
            if 'green' in action:
                action_col = 'green'
            if 'red' in action:
                action_col = 'red'

            if 'blue' in topcard:
                topcard_col = 'blue'
            if 'yellow' in topcard:
                topcard_col = 'yellow'
            if 'green' in topcard:
                topcard_col = 'green'
            if 'red' in topcard:
                topcard_col = 'red'

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

            if '0' in topcard:
                topcard_num = '0'
            if '1' in topcard:
                topcard_num = '1'
            if ' 2' in topcard:
                topcard_num = '2'
            if '3' in topcard:
                topcard_num = '3'
            if '4' in topcard:
                topcard_num = '4'
            if '5' in topcard:
                topcard_num = '5'
            if '6' in topcard:
                topcard_num = '6'
            if '7' in topcard:
                topcard_num = '7'
            if '8' in topcard:
                topcard_num = '8'
            if '9' in topcard:
                topcard_num = '9'
            if 'skip' in topcard:
                topcard_num = 'skip'
            if 'reverse' in topcard:
                topcard_num = 'reverse'
            if '+2' in topcard:
                topcard_num = '+2'

            if action_col == topcard_col or action_num == topcard_num:
                enemydeck.remove(action)
                topcard = action
                turn = 'player'
                print(action_col, topcard_col, action_num, topcard_num)

    if playerdeck == []:
        print('You Win!!')
        break

    if enemydeck == []:
        print('You Lose:(')
        break

    if deck == []:
        if enemydeck > playerdeck:
            print('You Win!!')
            break
        else:
            print('You Lose:(')
            break

input()
print(textwrap.fill(deck, 40))
print()
print(topcard)
print(playerdeck)
print(enemydeck)
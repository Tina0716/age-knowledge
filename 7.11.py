roster = {}
num_pairs = 5
menu = {'a': 'Add player', 'd': 'Remove player', 'u': 'Update player rating', 'r': 'Output players above a rating',
        'o': 'Output roster', 'q': 'Quit'}
menu_item = ' '

for i in range(num_pairs):
    jersey_num = int(input('\nEnter player %d\'s jersey number:\n' % (i + 1)))
    player_rating = int(input('Enter player %d\'s rating:\n' % (i + 1)))

    roster[jersey_num] = player_rating

print('\nROSTER')

for rate, jersey in sorted(roster.items()):
    print('Jersey number: %d, Rating: %d' % (rate, jersey))

while menu_item != 'q':
    print('\nMENU')
    for char, option in menu.items():
        print('%s - %s' % (char, option))

    user_char = input('\nChoose an option:')

    if user_char == 'o':
        print('\nROSTER')
        for rate, jersey in sorted(roster.items()):
            print('Jersey number: %d, Rating: %d' % (rate, jersey))

    if user_char == 'a':
        new_jersey = int(input('\nEnter a new player\'s jersey number:\n'))
        new_rating = int(input('Enter the player\'s rating:\n'))

        roster[new_jersey] = new_rating

        print(roster)

    if user_char == 'd':
        player_remove = int(input('\nEnter a jersey number:\n'))
        del roster[player_remove]

        print(roster)

    if user_char == 'u':
        update_jersey = int(input('Enter a jersey number: \n'))
        update_rating = int(input('Enter a new rating for player: \n'))
        roster.update({update_jersey: update_rating})

    if user_char == 'r':
        user_rate = input('Enter a rating:\n')
        print('ABOVE %d\n' % (user_rate))
        for rate in roster.value():
            if rate > user_rate:
                print('Jersey number: %d, Rating: %d' % (rate, jersey))
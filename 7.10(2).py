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
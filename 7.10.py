dic={'a': 'Add player', 'd': 'Remove player','u': 'Update player rating','r': 'Output players above a rating','o': 'Output roster','q': 'Quit'}
print("menu",dic)
menu_item=''
while menu_item != 'q':
    print('\ndic')
    for char, option in dic.items():
        print('%s - %s' %(char, option))
    user_char = input('\nChoose an option:')
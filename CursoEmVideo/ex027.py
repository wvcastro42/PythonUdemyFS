name = input('Type your full name: ').lower().strip()

a_name = name.split(' ')

print('Your full name is: {}'.format(name))
print('Your first name is: {}'.format(a_name[0]))
print('Your last name is: {}'.format(a_name[-1]))

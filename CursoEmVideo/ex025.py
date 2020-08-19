def find_silva(string):
    if name.lower().find('silva') >= 0:
        return "your name have 'Silva!'"
    return "your name doesnt have..."

name = input('Type your full name: ').strip()

print(find_silva(name))

# or using "in"
print('Seu nome tem Silva? {}'.format('silva' in name.lower()))

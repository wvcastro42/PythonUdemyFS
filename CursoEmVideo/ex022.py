name = input('Writhe your full name: ').strip()

print(name.upper())
print(name.lower())
print(len(name) - name.count(' '))
print(len(name.split()[0]))

# ou busca pelo primeiro espaço
print(name.find(' '))

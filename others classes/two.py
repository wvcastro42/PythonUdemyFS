import one
print('Top level Two.py')
one.func()

if __name__ == '__main__':
    print("Two.py being run directly")
else:
    print("two is being imported")

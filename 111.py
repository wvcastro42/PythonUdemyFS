try:
    f = open('simple.txt', 'w')
    f.write("yes, you're!")
except IOError:
    print("Error: Could not find file to open...sorry!")
else:
    print("sucess!")
    f.close()
finally:
    print("I always work no matter what...")

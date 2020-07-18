# -*- coding: utf-8 -*-
#INHERITANCE
# class Animal():
#
#     def __init__(self):
#         print("Animal Created")
#
#     def who_am_i(self):
#         print("Animal")
#
#     def eat(self):
#         print("Eating...")
#
#
# class Dog(Animal):
#
#     def __init__(self):
#         # Animal.__init__(self)
#         print("Dog Created!")
#
#     def bark(self):
#         print("Wooof")
#
#     def eat(self):
#         print("Dog eating")
#
#
# my_dog = Dog()
# my_dog.who_am_i()
# my_dog.eat()
# my_dog.bark()
#

# SPECIAL METHODS
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        """Method that return a string representation of the class book"""
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

b = Book("Python", "José", 200)
print(b)

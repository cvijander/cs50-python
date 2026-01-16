"""
def hello():
    print("hello")

name = input("What's your name? ")

hello()

print(name)
"""

"""
def hello(to="world"):
    print("Hello,",to) 

hello()
name = input("What's your name? ")       
hello(name)
"""


def main():
    name = input("What is your name? ")
    hello(name)


def hello(to):
    print("hello",to) 


main()    
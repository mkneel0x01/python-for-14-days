#global variables

"""x = "apple"

def myfunc():
    print("I love " + x)

myfunc()"""

"""x = "apple"

def myfunc():
    x = "orange"
    print("I love " + x)

myfunc()
print("I love " + x)"""


#The global Keyword

def myfunc():
    global x
    x = "mango"

myfunc()
print("I love " + x)

x = "bannana"
def myfunc():
    global x
    x = "mango"

myfunc()
print("I love " + x)
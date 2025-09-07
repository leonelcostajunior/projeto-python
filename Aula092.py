x = 300

# def myfunc():
#     print(x)

# def myfunc():
#     x = 200
#     print(x)

# def myfunc():
#     global x
#     x = 300

def myfunc():
    global x
    x = 200
    print(x)

myfunc()
print(x)

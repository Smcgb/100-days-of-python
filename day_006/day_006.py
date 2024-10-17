def my_function():
    print("Hello")
    print("Bye")


my_function()

while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def right():
    turn_left()
    turn_left()
    turn_left()
        
a = 0 
while not at_goal():
    if (right_is_clear() and a < 4):
        right()
        move()
        a += 1
    elif front_is_clear():
        move()
        a = 0
    else:
        turn_left()
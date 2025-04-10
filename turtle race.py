import turtle
import random
screen=turtle.Screen()
screen.setup(width=500,height=500)
screen.title('TURTLE RACE....')
screen.bgcolor('light blue')
colours=['black','green','red','brown']
turtles=[]
user_choice=screen.textinput('choose ur turtle','black green red brown')
position=[100,50,0,-50]
for i in range(4):
    t=turtle.Turtle(shape='turtle')
    t.color(colours[i])
    t.penup()
    t.goto(-240,position[i])
    turtles.append(t)
race=True
print('RACE STARTED....')
while race:
    for  i in turtles:
        i.forward(random.randint(1,10))
        if i.xcor()>=230:
            race=False
            win_colour=i.pencolor()
            print(win_colour)
            if user_choice==win_colour:
                print('YOU WON THE RACE')
            else:
                print('YOU LOSE THE RACE')
print('RACE ENDED....')
#Import Turtle
import turtle as trtl

#Make a turtle
james = trtl.Turtle()

def drawsquare():
    for sides in range(4):
        james.forward(30)
        james.right(90)


drawsquare()
james.forward(60)
drawsquare()

wn = trtl.Screen()
wn.mainloop()
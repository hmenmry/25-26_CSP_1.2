#Import Turtle
import turtle as trtl

#Make a turtle
james = trtl.Turtle()

def drawsquare(length):
    for sides in range(4):
        james.forward(length)
        james.right(90)


drawsquare(61)
james.forward(60)
drawsquare(47)

wn = trtl.Screen()
wn.mainloop()
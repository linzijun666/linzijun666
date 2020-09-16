
#haonan
import turtle
turtle.screensize(800,800,"black")
turtle.pensize(2)

for i in range(300):
    if i<100:
        turtle.pensize(1)
    elif i<200:
        turtle.pensize(2)
    else:
        turtle.pensize(3)

        
    if i%6==0:
        turtle.pencolor("red")
    elif i%6==1:
        turtle.pencolor("yellow")
    elif i%6==2:
        turtle.pencolor("blue")
    elif i%6==3:
        turtle.pencolor("green")
    elif i%6==4:
        turtle.pencolor("orange")
    else:
        turtle.pencolor("purple")
    turtle.fd(i/2)
    turtle.left(61)


turtle.done()

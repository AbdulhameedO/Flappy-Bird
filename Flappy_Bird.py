import turtle
bird = turtle.Turtle()
pipe = turtle.Turtle()
pipe2 = turtle.Turtle()
pipedown = turtle.Turtle()
pipedown2 = turtle.Turtle()
loser=turtle.Turtle()
am=turtle.Screen()

am.title("Flapyn")
am.bgcolor("blue")
am.setup(height=700, width= 1000)
am.tracer(0)

bird.speed(0)
bird.color("yellow")
bird.shape("circle")
bird.penup()
bird.goto(-400,0)

pipe.speed(0)
pipe.color("green")
pipe.shape("square")
pipe.penup()
pipe.goto(400,-200)
pipe.shapesize(stretch_wid=20,stretch_len=2.5)

pipedown.speed(0)
pipedown.color("green")
pipedown.shape("square")
pipedown.penup()
pipedown.goto(400,250)
pipedown.shapesize(stretch_wid=10,stretch_len=2.5)

pipe2.speed(0)
pipe2.color("green")
pipe2.shape("square")
pipe2.penup()
pipe2.goto(0,-250)
pipe2.shapesize(stretch_wid=10,stretch_len=2.5)

pipedown2.speed(0)
pipedown2.color("green")
pipedown2.shape("square")
pipedown2.penup()
pipedown2.goto(0,200)
pipedown2.shapesize(stretch_wid=20,stretch_len=2.5)

loser.speed(0)
loser.color("red")
loser.penup()
loser.hideturtle()
loser.goto(0,0)

def JUMBAYA():
    bird.sety(bird.ycor()+80)
   
am.listen()
am.onkeypress(JUMBAYA,"space")

z=True
while z:
    am.update()

    bird.sety(bird.ycor()-0.5)
    
    if pipe.xcor()>-520:
        x=pipe.xcor()-0.5
        pipe.setx(x)
        pipedown.setx(x)
    else:
        pipe.setx(500)
        pipedown.setx(500)

    if pipe2.xcor()>-520:
        y=pipe2.xcor()-0.5
        pipe2.setx(y)
        pipedown2.setx(y)
    else:
        pipe2.setx(500)
        pipedown2.setx(500)
    
    bx=bird.xcor()
    by=bird.ycor()

    if bx< pipe2.xcor()+10 and bx> pipe2.xcor()-10 and ((by>pipe2.ycor() -100 and by<pipe2.ycor()+100) or (by>pipedown2.ycor()-200 and by<pipedown2.ycor()+200)):
            z=0
    elif bx< pipe.xcor()+10 and bx> pipe.xcor()-10 and ((by>pipe.ycor() -200 and by<pipe.ycor()+200) or (by>pipedown.ycor()-100 and by<pipedown.ycor()+100)):
            z=0


pipe.hideturtle()
pipe2.hideturtle()
pipedown.hideturtle()
pipedown2.hideturtle()
loser.showturtle()
loser.write("YOU ARE A FREAKIN LOSER",align="center",font=("Courier", 20, "normal")) 

am.exitonclick()
am.mainloop()
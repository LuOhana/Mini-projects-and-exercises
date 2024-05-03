from turtle import *
from random import randint

#drawing the race track

#classic shape turtle
speed(0)
penup()
goto(-140, 140)

#racing track

for step in range(15):
    write(step, align = "center")
    right(90)

    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    
    penup()
    backward(160)
    left(90)
    forward(20)
    pendown()


#creating a turtle called dave
dave=Turtle()
 
dave.color("red")
dave.pencolor("red")
dave.shape("turtle")
dave.penup()
dave.goto(-160,100)
dave.pendown()

#creating a turtle called bob
bob = Turtle()

bob.color("brown")
bob.pencolor("brown")
bob.shape("turtle")
bob.penup()
bob.goto(-160,70)
bob.pendown()

#creating a turtle called john
john = Turtle()

john.color("green")
john.pencolor("green")
john.shape("turtle")
john.penup() 
john.goto(-160,40)
john.pendown() 

#creating a turtle called eric
eric = Turtle()

eric.color("yellow")
eric.pencolor("yellow")
eric.shape("turtle")
eric.penup() 
eric.goto(-160,10)
eric.pendown()

#moving them all at once at random speed
for movement in range(100):
    dave.forward(randint(1,5))
    john.forward(randint(1,5))
    bob.forward(randint(1,5))
    eric.forward(randint(1,5))


#announcing the winner

choice = [(dave, john, bob, eric)]
winner = choice()
write(f"{winner} win")
print(f"{winner} turtle won the race!")


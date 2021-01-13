from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Place Your Bet!", "Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
turtles = []
y_coord = -100
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coord)
    y_coord += 40
    turtles.append(new_turtle)


valid_race = False
if user_bet:
    valid_race = True

winner = ""
while valid_race:
    for i in turtles:
        rng = random.randint(0, 10)
        i.forward(rng)
        if i.xcor() >= 230:
            winner = i.pencolor()
            valid_race = False
            break

screen.bye()
if winner == user_bet:
    print(f"Congrats! {winner} has won the race!")
else:
    print(f"Sorry, {winner} beat {user_bet} to the finish line!")


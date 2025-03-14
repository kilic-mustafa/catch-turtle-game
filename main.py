from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle Game")

score = 0
time_left = 30
can_click = True

t = Turtle()
t.shape("turtle")
t.color("green")
t.shapesize(2,2,2)
t.penup()
t.speed(0)

score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0,230)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

time_display = Turtle()
time_display.hideturtle()
time_display.penup()
time_display.goto(0, 260)
time_display.write(f"Time: {time_left}", align="center", font=("Arial", 16, "bold"))

def move_turtle():
    global can_click, time_left
    if time_left <= 0:
        return

    can_click = True
    x = randint(-260,260)
    y = randint(-260,260)
    t.goto(x,y)
    screen.ontimer(move_turtle,800)

def increase_score(x,y):
    global score, can_click
    if can_click and time_left > 0:
        score += 1
        can_click = False
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_display.clear()
        time_display.write(f"Time: {time_left}", align="center", font=("Arial", 16, "bold"))
        screen.ontimer(countdown,1000)
    else:
        t.hideturtle()
        game_over()

def game_over():
  game_over_text = Turtle()
  game_over_text.hideturtle()
  game_over_text.penup()
  game_over_text.goto(0,0)
  game_over_text.write(f"  Game Over!\nYour Score: {score}", align="center", font=("Arial", 18, "bold"))

t.onclick(increase_score)
move_turtle()
countdown()

screen.mainloop()
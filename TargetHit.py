# Chapter 3 Exercise 19
# Anthony McCann CPW 101 10/22/17
# ch_3_jrn5_ex19.py
# Program 3-9 hit_the_target.py
# The goal of this exercise was to edit the existing
# code for the 'Hit the Target Game' on page 145.

# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600      # Screen width
SCREEN_HEIGHT = 600     # Screen height
TARGET_LLEFT_X = 100    # Target's lower - left X
TARGET_LLEFT_Y = 250    # Target's lower - left Y
TARGET_WIDTH = 25       # Width of the target
FORCE_FACTOR = 30       # Arbitrary force factor
PROJECTILE_SPEED = 1    # Projectile's animation speed
NORTH = 90              # Angle of north direction
SOUTH = 270             # Angle of south direction
EAST = 0                # Angle of east direction
WEST = 180              # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.bgcolor('black')

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.pencolor('yellow')
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.end_fill()
turtle.penup()

# Draw the stars area one.
turtle.pencolor('white')
turtle.goto(100, -100)
turtle.forward(50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(25)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(50)
turtle.forward(75)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(75)
turtle.forward(75)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(100)
turtle.forward(20)
turtle.pendown()
turtle.dot()
turtle.penup()

# Draw the planets area one.
turtle.pencolor('black')
turtle.goto(-129, -270)
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.penup()

# Draw the stars area two.
turtle.pencolor('white')
turtle.goto(-100, -50)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(25)
turtle.forward(75)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(50)
turtle.forward(25)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(75)
turtle.forward(50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(100)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()

# Draw the planets area two.
turtle.pencolor('black')
turtle.goto(-200, 200)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.penup()

# Draw the stars area three.
turtle.pencolor('white')
turtle.goto(100, 50)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(25)
turtle.forward(75)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(50)
turtle.forward(25)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(75)
turtle.forward(50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(100)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(25)
turtle.forward(75)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(50)
turtle.forward(25)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(75)
turtle.forward(50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(100)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()

# Draw the planets area three.
turtle.pencolor('black')
turtle.goto(275, -150)
turtle.pendown()
turtle.fillcolor('brown')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.penup()

# Draw the stars area four.
turtle.pencolor('white')
turtle.goto(-60, 150)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(25)
turtle.forward(75)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(50)
turtle.forward(25)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(75)
turtle.forward(50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(100)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()

# Draw the ship.
turtle.pencolor('black')
turtle.goto(16, -16)
turtle.pendown()
turtle.fillcolor('gray')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.penup()
turtle.goto(8, -2)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()
turtle.goto(-35,-13)
turtle.pendown()
turtle.pencolor('black')
turtle.setheading(0)
turtle.forward(55)
turtle.penup()

# That's no moon!
turtle.goto(135,270)
turtle.pendown()
turtle.pencolor('white')
turtle.write("That's no moon!")
turtle.penup()

# Draw the stars area five.
turtle.pencolor('white')
turtle.goto(0, 0)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(25)
turtle.forward(75)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(50)
turtle.forward(25)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(75)
turtle.forward(50)
turtle.pendown()
turtle.dot()
turtle.penup()
turtle.left(100)
turtle.forward(100)
turtle.pendown()
turtle.dot()
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.pencolor('red')
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Letting the user know what is expected.
print()
print('The goal is to get your nose into the square.')
print('Getting just the wing tips or back end do NOT count!')
print('Good luck, have fun!')

# Get the angle and force from the user.
print()
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
elif (angle > 70):
        print('Try less angle!')
elif (angle < 63):
        print('Try more angle!')
elif (angle == 70 and
      force == 10):
        print('You overshot!')
        print('Try a bit less angle and less force!')
elif (angle == 70 and
      force <= 9):
        print('So close!')
        print('Try less angle!')
elif (angle == 70 and
      force <= 7):
        print('Try less angle and more force!')
elif (angle == 69 and
      force == 10):
        print('You overshot!')
        print('Try a bit less angle and less force!')
elif (angle == 69 and
      force <= 9):
        print('You came up short and a bit askew!')
        print('Try a bit less angle!')
elif (angle == 68 and
      force == 10):
        print('Just a smidge overshot!')
        print('Get your nose in there, try a bit less force!')
elif (angle == 68 and
      force <= 8):
        print('You came up short!')
        print('Try some more force!')
elif (angle == 67 and
      force == 10):
        print('You overshot!')
        print('Try less force and more or less angle!')
elif (angle == 67 and
      force <= 9):
        print('So close!')
        print('Try more force and more or less angle!')
elif (angle == 66 and
      force <= 9):
        print('Heading is good!')
        print('Just try more force and get your nose in there!')
elif (angle == 65 and
      force == 10):
        print('You overshot!')
        print('Try a bit more angle and less force!')
elif (angle == 65 and
      force <= 9 and
      force >= 8):
        print('So close!')
        print('Try more angle and more force!')
elif (angle == 65 and
      force <= 7):
        print('Try more angle and more force!')
elif (angle == 64 and
      force == 10):
        print('You overshot!')
        print('Try a bit more angle and less force!')
elif (angle == 64 and
      force <= 9 and
      force >= 8):
        print('So close!')
        print('Try more angle and more force!') 
elif (angle == 64 and
      force <= 7):
        print('Try more angle and more force!')
elif (angle == 63 and
      force == 10):
        print('You overshot!')
        print('Try a bit more angle and less force!')
elif (angle == 63 and
      force <= 9 and
      force >= 8):
        print('So close!')
        print('Try more angle and more force!')
elif (angle == 63 and
      force <= 7):
        print('Try more angle and more force!')
else:
        print('You missed the target.')

# Asks user to press ENTER to exit.
print()
input('Press ENTER to exit')

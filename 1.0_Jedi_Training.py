'''
1.0 Jedi Training (17pts)  Name:malachi buza


1. Define Forking (1pt): coping a repository from anothers github account to ones own account

2. Define Cloning (1pt): downloading a repository to my pc from my github to work

3. Define Branching (1pt):

4. Define Committing (1pt): 

5. Define Merging (1pt): 

6. Define Pushing (1pt):

7. Define Pull Request (1pt): a request to pull a piece of code into the big project on git


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle



yoda=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
yoda.pensize(3) # width of pen line
yoda.speed(10)  # speed of drawing. Go fast to not waste time.
yoda.color("#00FF00")
yoda.penup()
yoda.forward(50)


yoda.write('malachi',font=("Arial", 20, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing

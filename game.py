##Mini Project
'''
    This is the project which wil be the interesting game "COLOUR GAME".
    This is the best brain twister game which everyone played.
    In this game player has to enter color of the word that appears on the screen and hence the score increases by one, the total time to play this game is 30 seconds.
    Interface will display name of different colors in different colors. 
    Player has to identify the color and enter the correct color name to win the game.
'''
##Code
'''
import tkinter 
import random 

colours = ['Red','Blue','Green','Pink','Black', 
		'Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 30

# function that will start the game. 
def startGame(event): 
	
	if timeleft == 30:  
		countdown()  
		nextColour() 
#Shows Next color
def nextColour():  
	global score 
	global timeleft 
	if timeleft > 0: 
		e.focus_set() 
		if e.get().lower() == colours[1].lower(): 
			score += 1
		e.delete(0, tkinter.END) 
		random.shuffle(colours) 
		label.config(fg = str(colours[1]), text = str(colours[0])) 
		scoreLabel.config(text = "Score: " + str(score))

# Countdown timer function 
def countdown(): 

	global timeleft 
	if timeleft > 0:  
		timeleft -= 1
		timeLabel.config(text = "Time left: "+ str(timeleft))  
		timeLabel.after(1000, countdown) 
  
# for GUI window 
root = tkinter.Tk()  
root.title("COLOR GAME") 
root.geometry("500x300") 

#instructions label 
instructions = tkinter.Label(root, text = "Type in the colourof the words, and not the word text!",font = ('Comic Sans MS', 12)) 
instructions.pack() 

#score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('Comic Sans MS', 12)) 
scoreLabel.pack() 

#time left label 
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Comic Sans MS', 12)) 
timeLabel.pack() 

#label for displaying the colours 
label = tkinter.Label(root, font = ('Comic Sans MS', 60)) 
label.pack()  
e = tkinter.Entry(root) 
root.bind('<Return>', startGame) 
e.pack() 
e.focus_set()
# start the GUI 
root.mainloop() 
'''

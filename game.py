
from tkinter import *


class Game:
    def __init__(self, screen):
        self.frame = Frame(screen)
        self.frame.grid()

        # print the question
        self.message = NONE

        # Box for input
        self.answer = Entry(self.frame)
        self.answer.grid(row=0, column=1)
        # where answer are stored(set)
        self.printingmessage = StringVar()
        self.label = NONE

        # submit button
        self.showbutton = NONE

        #
        # self.quitbutton = Button(frame, text="quit", command=frame.quit)
        # self.quitbutton.grid(row=2)

    def Create_message(self, print=" "):
        """
        Print out whatever massage
        """
        self.message = Label(self.frame, text=print)
        self.message.grid(row=0)

    def button1(self):
        """
        Create the submit button on screen
        """                                                 # call function
        self.showbutton = Button(self.frame, text="submit", command=self.AskAnswer)
        self.showbutton.grid(row=0, column=2)

    def AskAnswer(self):
        """
        When button is pressed, get the item from the textbox
        """
        txt = self.answer.get()    # get item from user input box
        M = "Hi, {0}! Welcome to the game of nim!".format(txt)    # create a massage with input
        self.printingmessage.set(M)      # printingmessage set to message

    def PrintAnswer(self, response=""):
        """
        When function is called, print message on screen
        """
        self.printingmessage.set(response)  # get the printing massage
        self.label = Label(self.frame, textvariable=self.printingmessage)   # create label to print
        self.label.grid(row=3)


screen = Tk()
screen.minsize(width=550, height=100)
screen.maxsize(width=550, height=100)

G = Game(screen)    # call class
G.Create_message("what is your name?")
G.button1()
G.PrintAnswer()     # call function to print

# say = Label(screen, text="What's your name?")
# say.grid(row=1, sticky=E)
#
# answer = Entry(screen)
# answer.grid(row=1, column=1)

screen.mainloop()

#print text

#
# # Buttons
# myButton1 = Button(screen, text="Submit", command=PrintReply)
# myButton1.grid(row=1, column=2)



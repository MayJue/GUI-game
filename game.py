
from tkinter import *


class Game:
    def __init__(self, screen):
        self.frame = Frame(screen)
        self.frame.grid()

        # print the question
        self.message = Label(self.frame, text="What is your name?")
        self.message.grid(row=0)
        # Box for input
        self.answer = Entry(self.frame)
        self.answer.grid(row=0, column=1)
        # where answer are stored(set)
        self.printingmessage = StringVar()
        self.label = NONE

        # submit button                                    # call function
        self.showbutton = Button(self.frame, text="submit", command=self.AskAnswer)
        self.showbutton.grid(row=1)
        #
        # self.quitbutton = Button(frame, text="quit", command=frame.quit)
        # self.quitbutton.grid(row=2)

    def AskAnswer(self):
        """
        When button is pressed, get the item from the textbox
        """
        txt = self.answer.get()     # get item from user input box
        message = "Hi, {0}!".format(txt)    # create a massage with input
        self.printingmessage.set(message)      # printingmessage set to message

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



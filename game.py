
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
        self.state = "name"
        #
        # self.quitbutton = Button(frame, text="quit", command=frame.quit)
        # self.quitbutton.grid(row=2)
    def SetMessage(self, print=""):
        self.message.config(text=print)


    def Create_message(self, print=" "):
        """
        Print out whatever massage
        """
        self.message = Label(self.frame, text=print)
        self.message.grid(row=0)

    def button1(self):
        """
        Create the submit button on screen
        """

        # call function
        self.showbutton = Button(self.frame, text="submit", command=self.AskAnswer)
        self.showbutton.grid(row=0, column=2)

    def AskAnswer(self):
        """
        When button is pressed, get the item from the textbox
        """

        if self.state == "name":

            txt = self.answer.get()    # get item from user input box
            M = "Hi, {0}! Welcome to the game of nim!".format(txt)    # create a massage with input
            self.printingmessage.set(M)      # printingmessage set to message

            self.SetMessage("Choose a number greater than 14 to start with, what number would you like?")
            self.state = "starter number"
            self.answer.delete(0, 'end')

        elif self.state == "starter number":
            txt = self.answer.get()    # get item from user input box
            num = 0
            def isValid(num):
                if num <= 14:
                    return False
                return True

            try:
                num = int(txt)
                if not isValid(num):
                    raise Exception("That's not greater than 15, try a different number")
            except:
                M = "That's not a valid number, please enter a number greater than 14"
                self.printingmessage.set(M)
                self.answer.delete(0, 'end')
                return
            M = "You choose number {0}".format(txt)    # create a massage with input
            self.printingmessage.set(M)      # printingmessage set to message

            self.SetMessage("Choose a number 1-4 to take away")
            self.state = "number"
            self.answer.delete(0, 'end')

        elif self.state == "number":
            txt = self.answer.get()    # get item from user input box
            num = 0
            def isValid(num):
                if num <= 0 or num > 4:
                    return False
                return True

            try:
                num = int(txt)
                if not isValid(num):
                    raise Exception("not valid number")
            except:
                M = "That's not a valid number, enter a number between 1-4"
                self.answer.delete(0, 'end')
                return
            M = "You choose number {0}".format(txt)    # create a massage with input
            self.printingmessage.set(M)      # printingmessage set to message

            self.SetMessage("what number would you like to start with?")
            self.state = "number"
            self.answer.delete(0, 'end')

    def PrintAnswer(self, response=""):
        """
        When function is called, print message on screen
        """
        self.printingmessage.set(response)  # get the printing massage
        self.label = Label(self.frame, textvariable=self.printingmessage)   # create label to print
        self.label.grid(row=3)


def main():
    screen = Tk()
    screen.minsize(width=700, height=100)
    screen.maxsize(width=700, height=100)

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

if __name__ == "__main__":
    main()
#print text

#
# # Buttons
# myButton1 = Button(screen, text="Submit", command=PrintReply)
# myButton1.grid(row=1, column=2)



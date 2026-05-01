from tkinter import *
from vote_logic import *

class Gui:
    def __init__(self, window):
        self.window = window

        #TITLE
        self.label_title = Label(self.window, text='VOTING APPLICATION')
        self.label_title.pack(side='top', pady=10)
        
        #ID
        self.frame_id = Frame(self.window)
        self.label_id = Label(self.frame_id, text='ID')
        self.entry_id = Entry(self.frame_id, width=20)
        self.label_id.pack(padx= 5, side='left')
        self.entry_id.pack(padx=5, side='left')
        self.frame_id.pack(pady=10)
        

        #Canidates
        self.frame_can = Frame(self.window)
        self.label_can = Label(self.frame_can, text='CANIDATES')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_can1 = Radiobutton(self.frame_can, text='Jane', variable=self.radio_1, value=1)
        self.radio_can2 = Radiobutton(self.frame_can, text='John', variable=self.radio_1, value=2)
        self.label_can.pack(side='top', pady=5)
        self.radio_can1.pack(side='top', pady=5)
        self.radio_can2.pack(side='top', pady=5)
        self.frame_can.pack(pady=10)

        #Submit
        self.frame_sub = Frame(self.window)
        self.button_sub = Button(self.frame_sub, text='SUBMIT VOTE', command=self.voted)
        self.button_sub.pack(pady=10)
        self.frame_sub.pack()

        #Result Button
        self.frame_result = Frame(self.window)
        self.button_result = Button(self.frame_sub, text='VIEW CURRENT RESULTS', command=self.result)
        self.button_result.pack(pady=10)
        self.frame_result.pack()

        #error label - reused for valid votes and voting poll status.
        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error)
        self.label_error.pack(pady=10)
        self.frame_error.pack()


    def voted(self) -> None:
        """
        Function used when user clicks the submit button. 
        Function grabs users ID and selected canidate, then passes these values to the pick()
        function for storage. 
        """
        try:
            id = self.entry_id.get().strip()
            choice = self.radio_1.get()

            pick(id,choice)
            self.label_error.config(text='Thanks for Voting!', fg="green")

            self.entry_id.delete(0, END)
            self.radio_1.set(0)

        except ValueError:
            self.label_error.config(text='You Already Voted', fg="red")

        except TypeError:
            self.label_error.config(text='ID must be an integer between 1-9999', fg='red')

        except NameError:
            self.label_error.config(text='Must select a canidate!', fg='red')


    def result(self) -> None:
        """
        Function is used with the total button, when clicked, the function runs the total function pull count 
        of total votes for each canidate and total of all votes submitted 
        and stores the received values in variables jane, john, and total_count
        Finally it displays these values back to the user
        """
        jane, john, total_count = total()
        self.label_error.config(text=f"Jane: {jane} | John: {john} | Total Votes: {total_count}", fg='green')

                





            




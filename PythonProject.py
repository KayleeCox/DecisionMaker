
import tkinter
from random import randint


class DecisionMaker:
	def __init__(self, option_list):
		# Creating main window and input box
		self.main_window = tkinter.Tk()
		self.input_frame = tkinter.Frame(self.main_window)
		self.input_label = tkinter.Label(self.input_frame,
                                         text='Enter an option')
		self.input_entry = tkinter.Entry(self.input_frame,
                                         width=20)
		self.input_label.pack(side='left')
		self.input_entry.pack(side='left')
		self.input_frame.pack()
			
		#Create decision text
		self.decision_frame = tkinter.Frame(self.main_window)
		self.decision_label = tkinter.Label(self.decision_frame,
                                          text='Decision:')
		self.decision = tkinter.StringVar()
		self.actual_decision_label = tkinter.Label(self.decision_frame,
                                       textvariable=self.decision)
		self.decision_label.pack(side = 'left')
		self.actual_decision_label.pack(side = 'left')
		self.decision_frame.pack()

		#Creating button to add stuff
		self.button_frame = tkinter.Frame(self.main_window)
		self.add_button = tkinter.Button(self.button_frame, \
                                        text='Add', \
                                        command=self.add_option)
		self.add_button.pack(side = 'left')
        
        #Create decision button
		self.decision_button = tkinter.Button(self.button_frame, \
                                        text='Decide', \
                                        command=self.make_decision)
		self.decision_button.pack(side = 'right')
		self.button_frame.pack()
		
		#Create entry for list name
		self.input_list_frame = tkinter.Frame(self.main_window)
		self.input_list_label = tkinter.Label(self.input_list_frame,
                                         text='Enter list file name')
		self.input_list_entry = tkinter.Entry(self.input_list_frame,
                                         width=20)
		self.input_list_label.pack(side='left')
		self.input_list_entry.pack(side='left')
		self.input_list_frame.pack()
		
		#Create add list button
		self.list_button_frame = tkinter.Frame(self.main_window)
		self.add_list_button = tkinter.Button(self.list_button_frame, \
										text = "Add list", \
										command = self.get_list)
		self.add_list_button.pack()
		self.list_button_frame.pack()
		
		#The list that will hold the options
		self.option_list = option_list
		
		# Enter the tkinter main loop.
		tkinter.mainloop()


    
	def add_option(self):
		self.option = self.input_entry.get()
		self.option_list.append(self.option)
		self.input_entry.delete(0, 'end')
		
        
        
        
	def make_decision(self):
		index = randint(0, len(self.option_list) - 1)
		self.dec = self.option_list[index]
		self.decision.set(self.dec)
		
	def get_list(self):
		filename = self.input_list_entry.get()
		options_file = open(filename, "r")
		self.option_list = [line.rstrip() for line in options_file]
		options_file.close()


def main():
	options = []
	MyDecisionMaker = DecisionMaker(options)
	options_file = open("MyOptions.txt", "w+")
	for i in options:
		options_file.write(i + "\n")
		
	options_file.close()
	print("A list of your options is located in a file named MyOptions.txt")
		
	
main()

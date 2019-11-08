import tkinter as tk
from tkinter import *

class MainGUI:
	def __init__(self, master, controller):	 
		self.master = master			
		self.controller = controller
		self.mainColor = "#4682B4"
		self.query = ""

		# =========================
		# START: MAIN FRAME
		# =========================
		self.frame = Frame(master, width=800, height=600, bg=self.mainColor)
		self.frame.pack(fill="both", expand=True)
		self.frame.grid_propagate(False)
		self.frame.grid_rowconfigure(0, weight=1)
		self.frame.grid_columnconfigure(0, weight=1)

		# ================================
		# START: TOP PANE
		# ================================
		self.topPane = PanedWindow(self.frame, orient=HORIZONTAL)
		self.topPane.grid(row=0, sticky="nsew", pady=10)

		self.inputQueryEntry = Text(self.topPane, height=10, width=50)
		self.inputQueryEntry.grid(row=1, column=0, sticky="nsew")

		self.executeButton = Button(self.topPane, text="EXECUTE", command=self.executeQuery)
		self.executeButton.grid(row=1, column=1, sticky="nsew")
		# ================================
		# END: TOP PANE
		# ================================

		
		# ================================
		# START: BOTTOM PANE
		# ================================
		self.botPane = PanedWindow(self.frame, orient=HORIZONTAL)
		self.botPane.grid(row=1, sticky="new", pady=10)

		self.outputText = Label(self.botPane, height=20)
		self.outputText.grid(row = 0, column = 0, sticky="nsew")
		# self.outputText.config(state=DISABLED)

		# self.scrollbar = Scrollbar(self.botPane,command=self.outputText.yview)
		# self.outputText["yscrollcommand"] = self.scrollbar.set
		# self.scrollbar.grid(row = 0, column = 1, sticky="nsew")
		# ================================
		# END: BOTTOM PANE
		# ================================
		# ================================
		# END: MAIN FRAME
		# ================================

	# ================================
	# BUTTON COMMANDS
	# ================================
	def executeQuery(self):
		self.query1 = self.inputQueryEntry.get("1.0", "end-1c")
		self.controller.sendMessage(self, self.query1)
		

	def displayOutput(self, output):
		# self.outputText.delete(0,END)
		print(output)				
		self.outputText["text"] = output
			

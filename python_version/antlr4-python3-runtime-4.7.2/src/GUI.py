import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
from ImportCSV import CSVImport
from GenerateCSV import GenerateRecord

IMPORT_FILE_LOC = "import_files/"

class MainGUI:
	def __init__(self, master, controller):	 
		self.imp = CSVImport
		self.master = master			
		self.controller = controller
		self.mainColor = "#4682B4"
		self.query = ""
		self.messagebox = messagebox

		# =========================
		# START: MAIN FRAME
		# =========================
		self.frame = Frame(master, width=800, height=600, bg=self.mainColor)
		self.frame.pack(fill="both", expand=True)
		self.frame.grid_propagate(False)
		self.frame.grid_rowconfigure(0, weight=1)
		self.frame.grid_columnconfigure(0, weight=1)


		# =========================
		# START: MENU BAR
		# =========================
		menubar = Menu(master)
		filemenu = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="File", menu=filemenu)
		filemenu.add_command(label="Generate CSV", command=self.generateCSVDialog)
		filemenu.add_command(label="Import CSV", command=self. importFileDialog)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=master.quit)
		master.config(menu=menubar)
		# =========================
		# END: MENU BAR
		# =========================

		# ================================
		# START: TOP PANE
		# ================================
		self.topPane = PanedWindow(self.frame, orient=HORIZONTAL)
		self.topPane.grid(row=0, sticky="nsew", pady=10)

		self.inputQueryEntry = Text(self.topPane, height=10, width=50)
		self.inputQueryEntry.grid(row=1, column=0, sticky="nsew")		
	
		self.executeButton = Button(self.topPane, text="EXECUTE", command=self.executeQuery)
		self.executeButton.grid(row=1, column=1, sticky="nsew")

		self.clearButton = Button(self.topPane, text="CLEAR", command=self.clearQuery)
		self.clearButton.grid(row=1, column=2, sticky="nsew")
		# ================================
		# END: TOP PANE
		# ================================

		
		# ================================
		# START: BOTTOM PANE
		# ================================
		self.botPane = PanedWindow(self.frame, orient=HORIZONTAL)
		self.botPane.grid(row=1, sticky="new", pady=10)

		self.outputText = Text(self.botPane, height=20)
		self.outputText.grid(row = 0, column = 0, sticky="nsew")

		self.scrollbar = Scrollbar(self.botPane, command=self.outputText.yview)
		self.outputText["yscrollcommand"] = self.scrollbar.set
		self.scrollbar.grid(row = 0, column = 1, sticky="nsew")

		self.clearButton1 = Button(self.botPane, text="CLEAR", command=self.clearResult)
		self.clearButton1.grid(row=1, column=2, sticky="nsew")
		# ================================
		# END: BOTTOM PANE
		# ================================
		# ================================
		# END: MAIN FRAME
		# ================================

	# ================================
	# BUTTON COMMANDS
	# ================================
	
	# ================================
	# FUNC: SEND THE QUERY TO CONTROLLER 
	# ================================
	def executeQuery(self):
		self.query1 = self.inputQueryEntry.get("1.0", "end-1c")
		self.controller.sendMessage(self, self.query1)

	# ================================
	# FUNC: CLEAR TEXT 
	# ================================
	def clearQuery(self):
		self.inputQueryEntry.delete("1.0", "end-1c")

	def clearResult(self):
		self.outputText.config(state=NORMAL)
		self.outputText.delete("1.0", "end-1c")
		self.outputText.config(state=DISABLED)
		
	# ================================
	# FUNC: DISPLAY RESULTS TO UI 
	# ================================
	def displayOutput(self, output):
		self.outputText.config(state=NORMAL)
		self.outputText.insert(END, output+'\n\n\n')
		self.outputText.config(state=DISABLED)
			
	def importFileDialog(self):
		filename =  filedialog.askopenfilename(initialdir = IMPORT_FILE_LOC, title = "SELECT FILE TO IMPORT",filetypes = (("CSV FILE","*.csv"),("ALL FILES","*.*")))
		result = self.imp.main(self, filename)
		for key,val in result.items():			
			if key:
				self.messagebox.showinfo('IMPORTING CSV FILE...', val)
			else:
				self.messagebox.showerror('IMPORTING CSV FILE...', val)

	def generateCSVDialog(self):
		self.status = False
		self.msg = ''

		try:
			d = MyDialog(self.master)
			table = d.result[0][0]
			column = d.result[1][0]
			primary_key = d.result[2][0]
			count = d.result[3][0]		

			if table == False and column == False and count == False:
				self.status = False
				self.msg = "PLEASE FILL REQUIRED FIELD/S."
			else:
				if table == False:
					self.status = False
					self.msg = "NO TABLE SET."
				elif column == False:
					self.status = False
					self.msg = "NO COLUMN SET OR INVALID DATA TYPE."
				elif count == False:
					self.status = False
					self.msg = "NO ROW COUNT SET."
				else:
					self.status = True
					self.msg = "RECORD/S GENERATED SUCCESSFULLY."
					gen_csv = GenerateRecord
					gen_csv.main(self, table, column, primary_key, count)
			
			if self.status:
				self.messagebox.showinfo('GENERATING CSV FILE...', self.msg)
			else:
				self.messagebox.showerror('GENERATING CSV FILE...', self.msg)
		except:
			pass
		

class MyDialog(simpledialog.Dialog):

	def body(self, master):
		self.frame = Frame(master, width=400, height=200)
		self.frame.pack(fill="both", expand=True)
		self.frame.grid_propagate(False)
		# self.frame.grid_rowconfigure(0, weight=1)
		# self.frame.grid_columnconfigure(0, weight=1)

		self.tableLabel = Label(self.frame, text="Table Name:")
		self.tableLabel.grid(row = 0, column = 0, sticky="nsew")
		self.columnLabel = Label(self.frame, text="Column Name:")
		self.columnLabel.grid(row = 1, column = 0, sticky="nsew")
		self.primaryKeyLabel = Label(self.frame, text="Primary Key:")
		self.primaryKeyLabel.grid(row = 2, column = 0, sticky="nsew")
		self.countLabel = Label(self.frame, text="Primary Key:")
		self.countLabel.grid(row = 3, column = 0, sticky="nsew")

		self.tableEntry = Entry(self.frame)
		self.tableEntry.grid(row = 0, column = 1, sticky="nsew")
		self.tableEntry.insert(0,"imp_csv")

		self.columnEntry = Entry(self.frame)
		self.columnEntry.grid(row = 1, column = 1, sticky="nsew")
		self.columnEntry.insert(0,"id:float,fname:varchar,lname:varchar,age:float")

		self.primaryKeyEntry = Entry(self.frame)
		self.primaryKeyEntry.grid(row = 2, column = 1, sticky="nsew")
		self.primaryKeyEntry.insert(0,"id")

		self.countEntry = Entry(self.frame)
		self.countEntry.grid(row = 3, column = 1, sticky="nsew")
		self.countEntry.insert(0,"10")
		
		
		# return self.e1 # initial focus

	def apply(self):
		
		self.table = self.tableEntry.get()
		self.column = self.columnEntry.get()
		self.primary_key = self.primaryKeyEntry.get()
		self.count = self.countEntry.get()

		if self.table == '':
			self.table = False
		if self.column == '':
			self.column = False
		else:
			self.column = self.formatColumn(self.column)

		if self.count == '':
			self.count = False
		else:
			self.count = int(self.countEntry.get())
		
		self.result = [self.table], [self.column], [self.primary_key], [self.count]

	def formatColumn(self, column):
		col_type = {}
		valid_type = ["float", "varchar", "date"]
		for val in column.split(','):
			key = val.split(':')
			key_type = key[1].lower()
			if key_type not in valid_type:
				return False
			else:
				col_type[key[0].strip()] = key_type.strip()

		return col_type
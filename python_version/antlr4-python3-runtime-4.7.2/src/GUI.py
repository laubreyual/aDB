import tkinter as tk
import re
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
		self.topPane.grid(row=0, sticky="nsew")

		self.inputQueryEntry = Text(self.topPane, height=10, width=50)		
		self.inputQueryEntry.pack(fill="x", padx=20, pady=(10,0))	
	
		self.executeButton = Button(self.topPane, text="EXECUTE", height=2, width=20, bg="#6699ff", activebackground="#00ff99", command=self.executeQuery)		
		self.executeButton.pack(side=LEFT, padx=(20,5), pady=(10,10))

		self.clearButton = Button(self.topPane, text="CLEAR",  height=2, width=20, bg="#ffff66", activebackground="#00ff99", command=self.clearQuery)		
		self.clearButton.pack(side=LEFT, padx=(5,0), pady=(10,10))
		# ================================
		# END: TOP PANE
		# ================================

		# ================================
		# START: BOTTOM PANE
		# ================================
		self.botPane = PanedWindow(self.frame, orient=HORIZONTAL, bg=self.mainColor)
		self.botPane.grid(row=1, sticky="nsew", pady=(10, 10), padx=15)

		self.outputLabel = Label(self.botPane, text="OUTPUT WINDOW", font='Arial 12 bold', bg=self.mainColor, fg="#ffffff")
		self.outputLabel.grid(row=0, column=0, sticky="nsw", pady=(0,2))

		self.outputText = Text(self.botPane, height=17, width=93, wrap=NONE)
		self.outputText.grid(row = 1, column=0, sticky="nsew")	

		self.scrollbar = Scrollbar(self.botPane, command=self.outputText.yview, orient=VERTICAL)
		self.outputText["yscrollcommand"] = self.scrollbar.set
		self.scrollbar.grid(row = 1, column = 1, sticky="nsew")		
		
		self.scrollbarx = Scrollbar(self.botPane, command=self.outputText.xview, orient=HORIZONTAL)
		self.outputText["xscrollcommand"] = self.scrollbarx.set
		self.scrollbarx.grid(row = 2, column = 0, sticky="nsew")			

		self.clearButton1 = Button(self.botPane, text="CLEAR", height=1, width=15, bg="#ffff66", activebackground="#00ff99", command=self.clearResult)
		self.clearButton1.grid(row=3, column=0, pady=(10,0))		
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
		if len(self.query1) > 0:
			self.controller.sendMessage(self, self.query1)
		else:
			self.messagebox.showinfo('EXECUTE QUERY', "Nothing to execute.")

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
		self.headerTag = '--------------------------------------------------'
		self.outputHeader = self.headerTag + '\n QUERY: ' + self.query1 + '\n' + self.headerTag + '\n'
		self.outputText.insert("1.0", self.outputHeader + output + '\n\n\n')
		self.outputText.config(state=DISABLED)
			
	def importFileDialog(self):
		filename =  filedialog.askopenfilename(initialdir = IMPORT_FILE_LOC, title = "SELECT FILE TO IMPORT",filetypes = (("CSV FILE","*.csv"),("ALL FILES","*.*")))
				
		if filename == "":
			pass
		else:
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

		self.tableLabel = Label(self.frame, text="TABLE NAME:", anchor="w")
		self.tableLabel.pack(fill="both")
		self.tableEntry = Entry(self.frame, width=70, textvariable="table")
		self.tableEntry.pack(fill="x", pady=(2,15))
		self.tableEntry.insert(0,"imp_csv")

		self.columnLabel = Label(self.frame, text="COLUMN NAME:", anchor="w")
		self.columnLabel.pack(fill="both")
		self.columnLabel1 = Label(self.frame, text="FORMAT [col:type] OR [col1:type,col1:type] for multiple columns", anchor="w")
		self.columnLabel1.pack(fill="both")
		self.columnEntry = Entry(self.frame, width=70)
		self.columnEntry.pack(fill="x", pady=(2,15))
		self.columnEntry.insert(0,"id:float,fname:varchar,lname:varchar,age:float")
		
		self.primaryKeyLabel = Label(self.frame, text="PRIMARY KEY:", anchor="w")
		self.primaryKeyLabel.pack(fill="both")
		self.primaryKeyEntry = Entry(self.frame, width=70)
		self.primaryKeyEntry.pack(fill="x", pady=(2,15))
		self.primaryKeyEntry.insert(0,"id")
		
		self.countLabel = Label(self.frame, text="GENERATE NUMBER OF ROWS:", anchor="w")
		self.countLabel.pack(fill="both")		
		self.countEntry = Entry(self.frame, width=70)
		self.countEntry.pack(fill="x", pady=(2,15))		
		self.countEntry.insert(0,"10")	

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
		self.messagebox = messagebox
		
		col_type = {}
		valid_type = ["float", "varchar", "date"]
		try:
			for val in column.split(','):
				key = val.split(':')
				key_type = key[1].lower()
				if key_type not in valid_type:
					return False
				else:
					col_type[key[0].strip()] = key_type.strip()

			return col_type
		except:
			self.messagebox.showerror('GENERATING CSV FILE...', "INVALID COLUMNS FORMAT")
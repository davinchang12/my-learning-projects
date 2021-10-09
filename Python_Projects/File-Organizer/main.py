from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import _show

from file_organizer import FileOrganization

organizer = FileOrganization()

base = Tk()
base.geometry("550x100")
base.title("File Orgranizer")

check = 0
ext = ''

# Get option
def getOptionExt(select):
	ext = select

# Get path from current / destination directory
def getFolderPath(folder_path, curr_dest = 'curr'):
	# Get path
	folder_selected = filedialog.askdirectory()
	folder_path.set(folder_selected)
	
	# If path is current path
	if folder_selected != '' and curr_dest == 'curr':
		choose_ext = Label(base, text = "Choose Extensions : ")
		choose_ext.grid(row=4, column=0)

		# Get file extension in current directory 
		ext = organizer.getExtension(folder_selected)
		variable = StringVar(base)
		variable.trace_add('write', lambda *args: variable.get())
		
		# Try if there are file in the folder
		try:
			variable.set(ext[0])
			ext_menu = OptionMenu(base, variable, *ext, command=getOptionExt)
			ext_menu.grid(row=4, column=1)

			organize = ttk.Button(base, text="Organize",command= lambda : doOrganize(folder_path_current.get(), folder_path_destination.get(), variable.get()))
			organize.grid(row=4,column=2)
		except (IndexError):
			base.after(100, lambda: _show('', 'No file inside current directory!'))

# Organize files in directory
def doOrganize(current_directory, destination_directory, extenstion):
	organizer.organize(current_directory, destination_directory, extenstion)
	base.after(1000, lambda: _show('', 'Success'))

if __name__ == "__main__" : 

	# Get current directory
	folder_path_current = StringVar()
	current_directory = Label(base ,text="Current Directory")
	current_directory.grid(row=0,column = 0)

	c_directory = Entry(base,textvariable=folder_path_current, width = 50)
	c_directory.grid(row=0,column=1)

	c_getPath = ttk.Button(base, text="Browse Folder",command= lambda : getFolderPath(folder_path_current))
	c_getPath.grid(row=0,column=2)

	# Get destination directory
	folder_path_destination = StringVar()
	destination_directory = Label(base ,text="Destination Directory")
	destination_directory.grid(row=2,column = 0)

	d_directory = Entry(base,textvariable=folder_path_destination, width = 50)
	d_directory.grid(row=2,column=1)

	d_getPath = ttk.Button(base, text="Browse Folder",command= lambda : getFolderPath(folder_path_destination, 'dest'))
	d_getPath.grid(row=2,column=2)

	base.mainloop()
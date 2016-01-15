from Tkinter import *
from ttk import *
import os
import tkFileDialog
import mover
import threading

root_window = Tk()

root_window.title("folders.db merging utility")

old_database_path = ""
new_database_path = ""


def select_folder():
    folder_selection = ""
    while not os.path.exists(folder_selection):
        folder_selection = tkFileDialog.askopenfilename()
    return folder_selection


def select_folder_old_new_wrapper(selection):
    global old_database_path
    global new_database_path
    if selection is "old":
        old_database_path = select_folder()
    else:
        new_database_path = select_folder()


old_database_file_frame = Frame(root_window)
new_database_file_frame = Frame(root_window)
go_button_frame = Frame(root_window)
progress_bar_frame = Frame(root_window)

old_database_selection_button = Button(master=old_database_file_frame, command=select_folder_old_new_wrapper("old"))
new_database_selection_button = Button(master=new_database_file_frame, command=select_folder_old_new_wrapper("new"))


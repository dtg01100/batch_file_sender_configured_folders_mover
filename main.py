from Tkinter import *
from ttk import *
import os
import tkFileDialog
import mover

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
    global database_migrate_job
    if selection is "old":
        old_database_path = select_folder()
        old_database_label.configure(text=old_database_path)
    else:
        new_database_path = select_folder()
        new_database_label.configure(text=new_database_path)
    if os.path.exists(old_database_path) and os.path.exists(new_database_path):
        process_database_files_button.configure(state=NORMAL)
        database_migrate_job = mover.DbMigrationThing(old_database_path, new_database_path)


old_database_file_frame = Frame(root_window)
new_database_file_frame = Frame(root_window)
go_button_frame = Frame(root_window)
progress_bar_frame = Frame(root_window)

old_database_selection_button = Button(master=old_database_file_frame, text="Select Old Database File",
                                       command=lambda: select_folder_old_new_wrapper("old")).pack(anchor='w')

new_database_selection_button = Button(master=new_database_file_frame, text="Select New Database File",
                                       command=lambda: select_folder_old_new_wrapper("new")).pack(anchor='w')

old_database_label = Label(master=old_database_file_frame, text="No File Selected")
new_database_label = Label(master=new_database_file_frame, text="No File Selected")
old_database_label.pack(anchor='w')
new_database_label.pack(anchor='w')

process_database_files_button = Button(master=go_button_frame, text="Move Active Folders",
                                       command=lambda: database_migrate_job.do_migrate(progress_bar, root_window))

process_database_files_button.configure(state=DISABLED)

process_database_files_button.pack()

progress_bar = Progressbar(master=progress_bar_frame)
progress_bar.pack()

new_database_file_frame.pack(anchor='w')
old_database_file_frame.pack(anchor='w')
go_button_frame.pack(side=LEFT, anchor='w')
progress_bar_frame.pack(side=RIGHT, anchor='e')

root_window.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os.path
from os import path
import subprocess


root = Tk()


# RadioButton Frame
radiobutton_frame = ttk.Frame(root)
radiobutton_frame.pack(padx=10, pady=10)
# Entry Frame
entry_frame = ttk.Frame(root)
entry_frame.pack()
# Button Frame
button_frame = ttk.Frame(root)
button_frame.pack()

root.geometry('700x400')
root.title("AutoGit")
root.iconbitmap('./img/github.ico')

filePath = StringVar()
switch_variable = StringVar()
reponame = ''
pathVar = ''
gitUsername = ''
gitPassword = ''
removeRepo = ''


def switch():
    switchVar = switch_variable.get()
    if switchVar == 'create':
        removeProject.grid_forget()
        removeProjectEntry.grid_forget()
        removeButton.pack_forget()
        projectNameLabel.grid(row=2, column=0, padx=10, pady=10)
        projectNameEntry.grid(
            row=2, column=1, columnspan=2, padx=10, pady=10)
        pathLabel.grid(row=3, column=0, padx=10, pady=10)
        pathEntry.grid(
            row=3, column=1, columnspan=2, padx=10, pady=10)
        createButton.pack(
            side=RIGHT, padx=10, pady=10)
        browseButton.pack(
            side=RIGHT, padx=10, pady=10)
    elif switchVar == 'remove':
        projectNameLabel.grid_forget()
        projectNameEntry.grid_forget()
        pathLabel.grid_forget()
        pathEntry.grid_forget()
        createButton.pack_forget()
        browseButton.pack_forget()
        removeProject.grid(row=2, column=0, padx=10, pady=10)
        removeProjectEntry.grid(
            row=2, column=1, columnspan=2, padx=10, pady=10)
        removeButton.pack(
            side=RIGHT, padx=10, pady=10)


def browse():
    feedback = filedialog.askdirectory()
    filePath.set(feedback)


def getGit():
    username = gitUsernameEntry.get()
    password = gitPasswordEntry.get()
    return (username, password,)


def create():
    text = ''
    gitUsername, gitPassword = getGit()
    reponame = projectNameEntry.get()
    pathVar = pathEntry.get()

    if reponame == '':
        text = "Status :- Empty Repo/Project Name !"
    elif pathVar == '':
        text = "Status :- Path Empty !"
    elif gitUsername == '':
        text = "Status :- GitHub Username Empty !"
    elif gitPassword == '':
        text = "Status :- GitHub Password Empty !"
    elif pathVar != '':
        if path.exists(pathVar):
            text = "Status :- OK"
        else:
            text = "Status :- Path doesn't exist"
    else:
        text = "Status :- OK"
    statusLabel.configure(text=text)
    if text != "Status :- OK":
        return
    command = f"shell.sh {gitUsername} {gitPassword} {pathVar} {reponame}"
    subprocess.call(command, shell=True)
    statusLabel.configure(text=f"{reponame} Created.")


def remove():
    text = ''
    gitUsername, gitPassword = getGit()
    removeRepo = removeProjectEntry.get()
    if gitUsername == '':
        text = "Status :- GitHub Username Empty !"
    elif gitPassword == '':
        text = "Status :- GitHub Password Empty !"
    elif removeRepo == '':
        text = "Status :- GitHub Repository Empty !"
    else:
        text = "Status :- OK"
    statusLabel.configure(text=text)
    if text != "Status :- OK":
        return
    command = f"remove.py {gitUsername} {gitPassword} {removeRepo}"
    subprocess.call(command, shell=True)
    statusLabel.configure(text=f"{removeRepo} Removed.")

#       Radio Buttons
#       -------------


create_button = ttk.Radiobutton(radiobutton_frame, text="Create Repo", variable=switch_variable,
                                command=switch, value="create", width=18)
create_button.pack(side=LEFT)

remove_button = ttk.Radiobutton(radiobutton_frame, text="Remove Repo", variable=switch_variable,
                                command=switch, value="remove", width=18)
remove_button.pack(side=LEFT)

#           Git Username
#           ------------
gitUsernameLabel = ttk.Label(entry_frame, text="GitHub Username :").grid(
    row=0, column=0, padx=10, pady=10)
gitUsernameEntry = ttk.Entry(entry_frame, width=50)
gitUsernameEntry.grid(row=0, column=1, padx=10, pady=10)

#           Git Password
#           ------------

# Smiley \U0001F602
gitPasswordLabel = ttk.Label(entry_frame, text="GitHub Password :").grid(
    row=1, column=0, padx=10, pady=10)
gitPasswordEntry = ttk.Entry(entry_frame, width=50, show="=")
gitPasswordEntry.grid(row=1, column=1, padx=10, pady=10)

#       Project/Repository Name
#           ------------

projectNameLabel = ttk.Label(
    entry_frame, text="Project/Repo Name :")
projectNameEntry = ttk.Entry(entry_frame, width=50)


#          Path
#      -------------
pathLabel = ttk.Label(
    entry_frame, text="Path :")


pathEntry = ttk.Entry(entry_frame, width=50, textvariable=filePath)


#           Create Button
#        --------------------

createButton = ttk.Button(button_frame, text="Create", command=create)

#           Remove Button
#        --------------------

removeButton = ttk.Button(button_frame, text="Remove", command=remove)

#           Browse Button
#        --------------------

browseButton = ttk.Button(button_frame, text="Browse", command=browse)


#      Remove Project/Repository
#           ------------
removeProject = ttk.Label(
    entry_frame, text="Remove Repository :")
removeProjectEntry = ttk.Entry(entry_frame, width=50)


#               Status
#        --------------------
statusLabel = ttk.Label(entry_frame, text="Status :-")
statusLabel.grid(row=5, column=0, padx=10, pady=10)


#           Status Bar
#        --------------------
statusbar = ttk.Label(root, text="Developed by Divyanshu Shekhar.",
                      relief=GROOVE, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

#           Version
#           -------
version_label = ttk.Label(root, text="Version 1.0.1", relief=RIDGE, anchor=E)
version_label.pack(side=BOTTOM, fill=X)

root.mainloop()

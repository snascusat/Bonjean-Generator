import customtkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from excel import bonjeanGenerator
import os


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Bonjean Generator")

offset = []
savePath = []

def selectFile():
    global offset
    filetypes = filetypes=[("Excel Files", "*.xlsx;*.xls")]

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    offset = filename

    showinfo(
        title='Selected File',
        message=filename
    )

def selectFolder():
    global savePath
    foldername = fd.askdirectory()
    savePath = foldername

    showinfo(
        title='Selected Path',
        message=foldername
    )


def onGenerate(offset, savePath, depth):
    if not depth:
        showinfo(
            title='Error',
            message='You have not entered the depth of the vessel.'
        )

    bonjeanGenerator(offset, savePath, depth)
    file = 'bonjeanSheet.xlsx'
    path = os.path.join(savePath, file)

    if os.path.exists(path):   
        showinfo(
            title='Bonjean Excel File Saved',
            message='File saved at '+ savePath
        )
    else:
        showinfo(
            title='Error',
            message='Your file is not saved. There must be some error.'
        )


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome", font=("Roboto", 24))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Select Offset Table", command=selectFile)
button.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Depth of the vessel")
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Select folder to save bonjean", command=selectFolder)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkButton(master=frame, text="Generate Bonjean", command= lambda: onGenerate(offset, savePath, entry.get()))
checkbox.pack(pady=12, padx=10)

creditz = customtkinter.CTkLabel(master=frame, text=' Made with 💙 by mhdseby \n Powered by Royal Shippies ', )
creditz.place(relx=0.5, rely=1.0, anchor="s")

root.mainloop()
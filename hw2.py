from tkinter import *

main = Tk()
main.title("tk")
main.geometry("400x400")

titleLabel = Label(main, text="My APP", bg="black", fg="white", font=("Arial", 16))
titleLabel.grid(row=0, column=0, sticky="ew")

nameLabel = Label(main, text="Name")
nameLabel.grid(row=1, column=0, pady=30)
nameEntry = Entry(main)
nameEntry.grid(row=1, column=1, padx=20)

EmailLabel = Label(main, text="Email")
EmailLabel.grid(row=2, column=0)
EmailEntry = Entry(main)
EmailEntry.grid(row=2, column=1, padx=30)

passwordLab = Label(main, text="Password")
passwordLab.grid(row=3, column=0, pady=20, padx=10)
passwordEntry = Entry(main, show="*")
passwordEntry.grid(row=3, column=1, padx=30)

main.mainloop()
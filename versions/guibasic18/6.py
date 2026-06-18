import tkinter as tk

# setup window
wdow = tk.Tk ()
wdow.title("Party Hire")

#new hire title --row 0
tk.Label(text="New Hires", font=("Arial", 20)).grid(row=0, columnspan=2)

#name entry --row 1
tk.Label(text="Enter Full Name:").grid(row=1, column=0)

#receipt number --row 2
tk.Label(text="Enter Receipt #:").grid(row=2, column=0)

#Item hired (dropdown) --row 3
tk.Label(text="Item Hired:").grid(row=3, column=0)

#Number hired --row 4
tk.Label(text="# of Items Hired:").grid(row=4, column=0)

#submit button --row 5
tk.Button(text="Submit").grid(row=5, columnspan=2) #add command for function!!!

#return label --row 6
tk.Label(text="Returns").grid(row=6, columnspan=2)

#return name box --row 7
tk.Label(text="Name:").grid(row=7, column=0)

#return button --row 8
tk.Button(text="Return").grid(row=8, columnspan=2)

wdow.mainloop()
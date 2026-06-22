import tkinter as tk

names_list = [""]

def check_inputs(name):
    if name == "":
        tk.Label(text="Can't be blank", fg="Red").grid(row=1, column=2)
    else:
        print() # check receipt number

    names_list.append(name) # put at end of if later

def new_hire():
    name = full_name.get()
    #add receiptno, item, and n_hired
    print(name) # remove later
    check_inputs(name)

def returns():
    print()

hireables = ["Please Select", "Bouncy Castle", "Hats", "Plates", "Spoons"] #change for actual items

# setup window
box = tk.Tk ()
box.title("Party Hire")

# housekeeping ✌️
item_hired = tk.StringVar(value=hireables[0])

#new hire title --row 0
tk.Label(text="New Hires", font=("Arial", 20)).grid(row=0, columnspan=2)

#name entry --row 1
tk.Label(text="Enter Full Name:").grid(row=1, column=0)
full_name = tk.Entry()
full_name.grid(row=1, column=1)

#receipt number --row 2
tk.Label(text="Enter Receipt #:").grid(row=2, column=0)
receipt = tk.Entry()
receipt.grid(row=2, column=1)


#Item hired (dropdown) --row 3
tk.Label(text="Item Hired:").grid(row=3, column=0)
item_taken = tk.OptionMenu(box, item_hired, *hireables)
item_taken.grid(row=3, column=1)

#Number hired --row 4
tk.Label(text="# of Items Hired:").grid(row=4, column=0)
number_hired = tk.Entry()
number_hired.grid(row=4, column=1)

#submit button --row 5
tk.Button(text="Submit", command=new_hire).grid(row=5, columnspan=2)

#return label --row 6
tk.Label(text="Returns", font=("Arial", 20)).grid(row=6, columnspan=2)

#return name dropdown --row 7
tk.Label(text="Name:").grid(row=7, column=0)
return_item = tk.OptionMenu(box, hireables, *names_list)
return_item.grid(row=7, column=1)

#return button --row 8
tk.Button(text="Return", command=returns).grid(row=8, columnspan=2)

box.mainloop()
import tkinter as tk

hireables = ["Please Select", "Bouncy Castle", "Hats", "Plates", "Spoons"] #change for actual items
names_list = [""]
receipt_numbers = []

MAX_HIRED = 500

def save_to_file(name, receipt_int, item, n_hired):
    print() # save info to file in format
    # (name)
    #     (recipt number)
    #     (item hired)
    #     (number of items hired)
    names_list.append(name)
    receipt_numbers.append(receipt_int)
    with open("records.txt", "a") as file:
        file.write(f"{name}:\n")
        file.write(f"   Receipt Number:  {receipt_int}\n")
        file.write(f"   Item Hired:      {item}\n")
        file.write(f"   Number of Items: {n_hired}\n\n")

def check_inputs(name, receipt_str, item, number_hired):
    if name == "":
        tk.Label(text="Can't be blank", fg="Red").grid(row=1, column=2)
    else:
        try:
            receipt_int = int(receipt_str)
            if receipt_int in receipt_numbers:
                tk.Label(text = "Receipt number already used", fg="red").grid(row=2, column=2)
            else:
                try:
                    n_hired = int(number_hired)
                    if n_hired <= 0:
                        tk.Label(text = "Please enter a number over 1", fg="red").grid(row=4, column=2)
                    elif n_hired >> MAX_HIRED:
                        tk.Label(text = "Please enter a number less than 500", fg="red").grid(row=4, column=2)
                    else:
                        save_to_file(name, receipt_int, item, n_hired)
                        print()#done uhh return to for next step
                except ValueError:
                    tk.Label(text = "Please enter a number", fg="red").grid(row=2, column=2)

        except ValueError:
            tk.Label(text = "Please enter a number", fg="red").grid(row=2, column=2)

def new_hire():
    name = full_name.get()
    receipt_str = receipt.get()
    item = item_hired.get()
    number_hired = n_hired.get()
    print(name) # remove later
    check_inputs(name, receipt_str, item, number_hired)

def returns():
    print()


# setup window / dropdowns
box = tk.Tk ()
box.title("Party Hire")
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
n_hired = tk.Entry()
n_hired.grid(row=4, column=1)

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
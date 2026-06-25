import tkinter as tk
from tkinter import ttk

MAX_HIRED = 500

hireables = ["Bouncy Castle", "Hats", "Plates", "Spoons"] #change for actual items
names_list = [] 
receipt_numbers = []

def save_to_file(name, receipt_int, item, no_hired):
    names_list.append(name)
    receipt_numbers.append(receipt_int)
    with open("records.txt", "a") as file: # writing to file
        file.write(f"{name}:\n")
        file.write(f"   Receipt Number:  {receipt_int}\n")
        file.write(f"   Item Hired:      {item}\n")
        file.write(f"   Number of Items: {no_hired}\n\n")
    return_item['values'] = names_list

def check_inputs(name, receipt_str, item, number_hired):
    if name == "":
        blank_name.config(text="Can't be blank")
    else:
        try:
            receipt_int = int(receipt_str)
            if receipt_int in receipt_numbers:
                repeat_receipt.config(text="Receipt number already used")
            elif receipt_int < 1:
                low_receipt.config(text="Please enter valid number")
            else:
                if item == "":
                    please_select.config(text="Please Select")
                else:
                    try:
                        no_hired = int(number_hired)
                        if no_hired <= 0:
                            low_n.config(text="Please enter a number over 1")
                        elif no_hired > MAX_HIRED:
                            high_n.config(text="Please enter a number less than 500")
                        else:
                            save_to_file(name, receipt_int, item, no_hired)
                            full_name.delete(0, tk.END)
                            receipt.delete(0, tk.END)   # clearing inputs
                            n_hired.delete(0, tk.END)
                    except ValueError:
                        wrong_n.config(text="Please enter an integer (no decimals)")
        except ValueError:
            wrong_receipt.config(text="Please enter an integer (no decimals)")
            #= tk.Label(text = "Please enter an integer (no decimals)", fg="red").grid(row=2, column=2)

def new_hire():
    blank_name.config(text="")
    repeat_receipt.config(text="")
    low_receipt.config(text="")
    please_select.config(text="")
    wrong_n.config(text="")
    low_n.config(text="")
    high_n.config(text="")
    wrong_receipt.config(text="")
    name = full_name.get()
    receipt_str = receipt.get()
    item = item_taken.get()
    number_hired = n_hired.get()
    check_inputs(name, receipt_str, item, number_hired)

def returns():
    return_name = return_item.get()
    names_list.remove(return_name)
    with open("records.txt", "r") as file:
        lines = file.readlines()
            
    for i in range(len(lines)):
        if lines[i].startswith(return_name + ":"):
            lines[i] = lines[i].strip() + "  RETUNED\n"
            break
        else:
            print()

    with open("records.txt", "w") as file:
        file.writelines(lines)
    
    return_item['values'] = names_list

    print()


# setup window
box = tk.Tk ()
box.title("Party Hire")

#error label setup
blank_name = tk.Label(box, text="", fg="red")
blank_name.grid(row=1, column=2)
repeat_receipt = tk.Label(box, text = "", fg="red")
repeat_receipt.grid(row=2, column=2)
low_receipt = tk.Label(box, text="", fg="red")
low_receipt.grid(row=2, column=2)
please_select = tk.Label(text="", fg="red")
please_select.grid(row=3, column=2)
wrong_n = tk.Label(box, text = "", fg="red")
wrong_n.grid(row=4, column=2)
low_n = tk.Label(box, text = "", fg="red")
low_n.grid(row=4, column=2)
high_n = tk.Label(box, text = "", fg="red")
high_n.grid(row=4, column=2)
wrong_receipt = tk.Label(box, text = "", fg="red")
wrong_receipt.grid(row=2, column=2)

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
item_taken = ttk.Combobox(box, values=hireables, state="readonly")
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
return_item = ttk.Combobox(box, values=names_list, state="readonly")
return_item.grid(row=7, column=1)

#return button --row 8
tk.Button(text="Return", command=returns).grid(row=8, columnspan=2)

box.mainloop()

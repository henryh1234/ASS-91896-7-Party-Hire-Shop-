"""gather and store Julie's hire shop sales, store on file."""
import tkinter as tk
from tkinter import ttk

MAX_HIRED = 500

# GUI colours
BG_C = "#32a5ed"
TEXT_C = "#000000"
ERROR_C = "#ff0000"
TEXTBOX_C = "#268bc9"

hireables = ["Bouncy Castle", "Hats", "Plates", "Spoons"]  # change for actual items
names_list = []
receipt_numbers = []


def save_to_file(name, receipt_int, item, no_hired):
    """Save to the file, records.txt."""
    names_list.append(name)
    receipt_numbers.append(receipt_int)
    with open("records.txt", "a") as file:  # writing to file
        file.write(f"{name}:\n")
        file.write(f"   Receipt Number:  {receipt_int}\n")
        file.write(f"   Item Hired:      {item}\n")
        file.write(f"   Number of Items: {no_hired}\n\n")
    return_item['values'] = names_list  # updates returns dropdown


def check_inputs(name, receipt_str, item, number_hired):
    """Check the inputs for invalid info."""
    if name == "":
        blank_name.config(text="Can't be blank")
    else:
        try:
            receipt_int = int(receipt_str)  # changing receipt from string to integer
            if receipt_int in receipt_numbers:
                wrong_receipt.config(text="Receipt number already used")
            elif receipt_int < 1:
                wrong_receipt.config(text="Please enter valid number")
            else:
                if item == "":
                    please_select.config(text="Please Select")  # blank name
                else:
                    try:
                        no_hired = int(number_hired)
                        if no_hired < 1:
                            wrong_n.config(text="Please enter a number over 1")
                        elif no_hired > MAX_HIRED:
                            wrong_n.config(text="Please enter a number less than 500")
                        else:
                            save_to_file(name, receipt_int, item, no_hired)
                            full_name.delete(0, tk.END)
                            receipt.delete(0, tk.END)   # clearing inputs
                            n_hired.delete(0, tk.END)
                    except ValueError:
                        wrong_n.config(text="Please enter an integer (no decimals)")
        except ValueError:
            wrong_receipt.config(text="Please enter an integer (no decimals)")


def new_hire():
    """Get inputs and clear errors."""
    name = full_name.get()
    receipt_str = receipt.get()
    item = item_taken.get()
    number_hired = n_hired.get()
    blank_name.config(text="")      #|
    please_select.config(text="")   #|
    wrong_n.config(text="")         #| clearing errors
    wrong_receipt.config(text="")   #|
    blank_return.config(text="")    #|

    check_inputs(name, receipt_str, item, number_hired)


def returns():
    """Remove from list and append returned on file."""
    return_name = return_item.get()
    if return_name == "":
        blank_return.config(text="Please Select")
    else:
        blank_return.config(text="")

    names_list.remove(return_name)  # get length of file
    with open("records.txt", "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):  # look for name in lines
        if lines[i].startswith(return_name + ":"):
            lines[i] = lines[i].strip() + "  RETUNED\n"
            break

    with open("records.txt", "w") as file:  # write RETURNED after name
        file.writelines(lines)

    return_item['values'] = names_list  # updates returns dropdown


# setup window
box = tk.Tk()
box.title("Party Hire")
box.config(bg=BG_C)

# error label setup
blank_name = tk.Label(box, text="", bg=BG_C, fg=ERROR_C)
blank_name.grid(row=1, column=2)
please_select = tk.Label(text="", bg=BG_C, fg=ERROR_C)
please_select.grid(row=3, column=2)
wrong_n = tk.Label(box, text="", bg=BG_C, fg=ERROR_C)
wrong_n.grid(row=4, column=2)
wrong_receipt = tk.Label(box, text="", bg=BG_C, fg=ERROR_C)
wrong_receipt.grid(row=2, column=2)
blank_return = tk.Label(box, text="", bg=BG_C, fg=ERROR_C)
blank_return.grid(row=7, column=2)

# new hire title --row 0
tk.Label(text="New Hires", font=("Arial", 20), bg=BG_C, fg=TEXT_C).grid(row=0, columnspan=2)

# name entry --row 1
tk.Label(text="Enter Full Name:", bg=BG_C, fg=TEXT_C).grid(row=1, column=0, pady=5)
full_name = tk.Entry(bg=TEXTBOX_C, fg=TEXT_C)
full_name.grid(row=1, column=1, pady=5)

# receipt number --row 2
tk.Label(text="Enter Receipt #:", bg=BG_C, fg=TEXT_C).grid(row=2, column=0, pady=5)
receipt = tk.Entry(bg=TEXTBOX_C, fg=TEXT_C)
receipt.grid(row=2, column=1, pady=5)


# Item hired (dropdown) --row 3
tk.Label(text="Item Hired:", bg=BG_C, fg=TEXT_C).grid(row=3, column=0, pady=5)
item_taken = ttk.Combobox(box, values=hireables, state="readonly")
item_taken.grid(row=3, column=1, pady=5)

# Number hired --row 4
tk.Label(text="# of Items Hired:", bg=BG_C, fg=TEXT_C).grid(row=4, column=0, pady=5)
n_hired = tk.Entry(bg=TEXTBOX_C, fg=TEXT_C)
n_hired.grid(row=4, column=1, pady=5)

# submit button --row 5
tk.Button(text="Submit", command=new_hire, bg=BG_C, fg=TEXT_C).grid(row=5, columnspan=2, pady=5)

# return label --row 6
tk.Label(text="Returns", font=("Arial", 20), bg=BG_C, fg=TEXT_C).grid(row=6, columnspan=2, pady=5)

# return name dropdown --row 7
tk.Label(text="Name:", bg=BG_C, fg=TEXT_C).grid(row=7, column=0, pady=5)
return_item = ttk.Combobox(box, values=names_list, state="readonly")
return_item.grid(row=7, column=1)

# return button --row 8
tk.Button(text="Return", command=returns, bg=BG_C, fg=TEXT_C).grid(row=8, columnspan=2, pady=5)

box.mainloop()

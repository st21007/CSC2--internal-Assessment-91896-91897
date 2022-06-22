########################################################################
###This program is so julia and her workers can track their items#######
########################################################################

# import tkinter so we can make a GUI
from tkinter import ttk
from tkinter import *

# quit subroutine


def quit():
    main_window.destroy()

    #store name 
def storename():
    print("*******************************")
    print("*** julies party hire store ***")
    print("*******************************")
    storename ()


# print details of store

def print_store_details():
    # these are the global variables that are used
    global j_names, total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Customer Full Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Recepit Number").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Number of items hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item hired").grid(column=4, row=7)
#
    # add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(store_details[name_count][0])).grid(
            column=1, row=name_count+8)
        Label(main_window, text=(store_details[name_count][1])).grid(
            column=2, row=name_count+8)
        Label(main_window, text=(store_details[name_count][2])).grid(
            column=3, row=name_count+8)
        Label(main_window, text=(store_details[name_count][3])).grid(
            column=4, row=name_count+8)
        name_count += 1

        # Check the inputs are all valid


def check_inputs():
    # these are the global variables that are used
    global store_details, entry_customer, entry_recepit, entry_number, entry_hired, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=0)
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)

     # Check that customers name is not blank, set error text if blank
    if len(entry_customer.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1
    # Check that recepit number is not blank, set error text if blank
    if len(entry_recepit.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1
    # Check the number of items is not blank and between 5 and 10, set error text if blank
    if (entry_number.get().isdigit()):
        if int(entry_number.get()) < 1 or int(entry_number.get()) > 500:
            Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=2)
        input_check = 1
    # Check that the item hired is not blank, set error text if blank
    if len(entry_hired.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
        append_name()


def append_name():
    # these are the global variables that are used
    global store_details, entry_customer, entry_recepit, entry_number, entry_hired, total_entries
    # append each item to its own area of the list
    store_details.append([entry_customer.get(), entry_recepit.get(),
                         entry_number.get(), entry_hired.get()])

     # clear the boxes
    entry_customer.delete(0, 'end')
    entry_recepit.delete(0, 'end')
    entry_number.delete(0, 'end')
    entry_hired.delete(0, 'end')
    total_entries += 1

def delete_row():
    # these are the global variables that are used
    global store_details, delete_item, total_entries, name_count
    # find which row is to be deleted and delete it
    del store_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=name_count+7)
    Label(main_window, text="       ").grid(column=1, row=name_count+7)
    Label(main_window, text="       ").grid(column=2, row=name_count+7)
    Label(main_window, text="       ").grid(column=3, row=name_count+7)
    Label(main_window, text="       ").grid(column=4, row=name_count+7)
    # print all the items in the list
    print_store_details()

    # create the buttons and labels


def setup_buttons():
    # these are the global variables that are used
    global store_details, entry_customer, entry_recepit, entry_number, entry_hired, total_entries, delete_item
    # create all the empty and default labels, buttons and entry boxes. Put them in the correct grid recepit 
    Label(main_window, text="Customer Full Name") .grid(column=0, row=0, sticky=E)
    entry_customer = Entry(main_window)
    entry_customer.grid(column=1, row=0)
    Label(main_window, text="Recepit Number") .grid(column=0, row=1, sticky=E)
    entry_recepit = Entry(main_window)
    entry_recepit.grid(column=1, row=1)
    Button(main_window, text="Quit", command=quit,
           width=10) .grid(column=4, row=0, sticky=E)
    Button(main_window, text="Append Details",
           command=check_inputs) .grid(column=3, row=1)
    Button(main_window, text="Print Details", command=print_store_details,
           width=10) .grid(column=4, row=1, sticky=E)
    Label(main_window, text="Number of items hired") .grid(column=0, row=2, sticky=E)
    entry_number = Entry(main_window)
    entry_number.grid(column=1, row=2)
    Label(main_window, text="item hired") .grid(column=0, row=3, sticky=E)
    hired= StringVar()
    entry_hired = ttk.Combobox(main_window, textvariable=hired, values=('Spoon', 'Cups', 'plates', 'ballons', 'Fairy lights', 'ballon garland', 'banners', 'streamers', 'confetti', 'wall decorations' ), state='readonly')
    entry_hired.grid(column=1,row=5)
    Label(main_window, text="Row #") .grid(column=3, row=2, sticky=E)
    delete_item = Entry(main_window)
    delete_item .grid(column=4, row=2)
    Button(main_window, text="Delete Row", command=delete_row,
           width=10) .grid(column=3, row=2, sticky=E)
    Label(main_window, text="               ") .grid(column=2, row=0)






# start the program running


def main():
    # these are the global variables that are used
    global main_window
    global store_details, entry_name, entry_age, entry_gender, total_entries
    # create empty list for store details and empty variable for entries in the list
    store_details = []
    total_entries = 0
    # create the GUI and start it up
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()


main()

    


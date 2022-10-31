# I create a GUI which is a mix between a standard registration form and a survey.
# The GUI is consisting of several widgets such as label, button, entry, combobox, check box, text and so on.
# Different frames have borders in different colors.
# GUI and Component Resizing like the video provided.
from tkinter import *
from tkinter import ttk
from tkinter import font


def button_check_handler(event):
    if event.widget.instate(statespec=["selected"]):
        check = "deselected"
    else:
        check = "selected"
    print(event.widget["text"] + " is " + check)


def button_upd_handler(event):
    print("Receive updates = " + event.widget["text"])


def button_ne_handler(event):
    print("Receive emails = " + event.widget["text"])


def button_released_handler(event):
    print(event.widget["text"] + " clicked")


def combobox_handler(event):
    print(" Selected = " + str(event.widget.get()))


def enter_press_entry_handler(event):
    print("Text entered = " + event.widget.get())


def enter_press_text_handler(event):
    print("Text entered = " + event.widget.get("1.0", END))


def main():
    root = Tk()

    # Put the main window in the center of the screen
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    # give equal weight to all four rows on root window
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    # one column
    root.columnconfigure(0, weight=1)
    # give this frame a pink border
    pink = Frame(root, highlightcolor="pink", highlightbackground="pink",  highlightthickness=5)
    # place pink frame on top on root

    pink.grid(row=0, column=0, sticky=N+S+E+W)
    # give equal weight to first five rows on pink frame

    pink.rowconfigure(0, weight=1)
    pink.rowconfigure(1, weight=1)
    pink.rowconfigure(2, weight=1)
    pink.rowconfigure(3, weight=1)
    pink.rowconfigure(4, weight=1)
    pink.rowconfigure(5)
    # two column
    pink.columnconfigure(0)
    pink.columnconfigure(1, weight=1)
    # attach labels, text_fields and a combo box to pink frame
    label1 = ttk.Label(pink, text="User Name:", font=font.Font(family="Times New Roman", size=12))
    label2 = ttk.Label(pink, text="First Name:", font=font.Font(family="Times New Roman", size=12))
    label3 = ttk.Label(pink, text="Last Name:", font=font.Font(family="Times New Roman", size=12))
    label4 = ttk.Label(pink, text="Password:", font=font.Font(family="Times New Roman", size=12))
    label5 = ttk.Label(pink, text="Favorite Color:", font=font.Font(family="Times New Roman", size=12))
    label6 = ttk.Label(pink, text="Account Options:", font=font.Font(family="Times New Roman", size=12))
    label7 = ttk.Label(pink, text="Sports (like to watch):", font=font.Font(family="Times New Roman", size=12))
    text_field1 = ttk.Entry(pink)
    text_field2 = ttk.Entry(pink)
    text_field3 = ttk.Entry(pink)
    # set the password field just show "*"
    text_field4 = ttk.Entry(pink, show="*")
    combo_box1 = ttk.Combobox(pink)
    combo_box1.state(["readonly"])
    combo_box1["values"] = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet", "White", "Black"]
    # how many elements to display at once
    combo_box1["height"] = 8
    # set current selected the first choice in the beginning
    combo_box1.current(0)
    # Press the <Enter> key to call the event handler
    text_field1.bind("<KeyPress-Return>", enter_press_entry_handler)
    text_field2.bind("<KeyPress-Return>", enter_press_entry_handler)
    text_field3.bind("<KeyPress-Return>", enter_press_entry_handler)
    text_field4.bind("<KeyPress-Return>", enter_press_entry_handler)
    # The combobox widgets generates a <<ComboboxSelected>> virtual event
    # WHEN the user selects an element from the list of values.
    combo_box1.bind("<<ComboboxSelected>>", combobox_handler)
    # Put labels, text_fields and a combo box on the correct location of pink frame and able for resizing
    label1.grid(row=0, column=0, sticky=N+S+E+W)
    label2.grid(row=1, column=0, sticky=N+S+E+W)
    label3.grid(row=2, column=0, sticky=N+S+E+W)
    label4.grid(row=3, column=0, sticky=N+S+E+W)
    label5.grid(row=4, column=0, sticky=N+S+E+W)
    label6.grid(row=5, column=0, sticky=N+S+E+W)
    text_field1.grid(row=0, column=1, sticky=N+S+E+W)
    text_field2.grid(row=1, column=1, sticky=N+S+E+W)
    text_field3.grid(row=2, column=1, sticky=N+S+E+W)
    text_field4.grid(row=3, column=1, sticky=N+S+E+W)
    combo_box1.grid(row=4, column=1, sticky=N+S+E+W)
    label7.grid(row=5, column=1, sticky=E)

    cyan = Frame(root, highlightcolor="cyan", highlightbackground="cyan",  highlightthickness=5)
    cyan.grid(row=1, column=0,  sticky=N+S+E+W)
    cyan.rowconfigure(0, weight=1)
    cyan.columnconfigure(0, weight=1)
    cyan.columnconfigure(1, weight=1)
    orange = Frame(cyan, highlightcolor="orange", highlightbackground="orange",  highlightthickness=5)
    # place orange frame on left on cyan frame
    orange.grid(row=0, column=0, stick=N+S+W)
    orange.rowconfigure(0, weight=1)
    orange.rowconfigure(1)
    orange.rowconfigure(2)
    orange.columnconfigure(0)
    orange.columnconfigure(1)
    label8 = ttk.Label(orange, text="Updates:", font=font.Font(family="Times New Roman", size=10))
    label9 = ttk.Label(orange, text="Notification Emails:", font=font.Font(family="Times New Roman", size=10))
    control_updates = IntVar()
    control_updates.set(0)
    radio_button1_upd = ttk.Radiobutton(orange, value="Yes", variable=control_updates, text="Yes")
    radio_button2_upd = ttk.Radiobutton(orange, value="No", variable=control_updates, text="No")
    control_notiem = IntVar()
    control_notiem.set(0)
    radio_button1_ne = ttk.Radiobutton(orange, value="Yes", variable=control_notiem, text="Yes")
    radio_button2_ne = ttk.Radiobutton(orange, value="No", variable=control_notiem, text="No")
    label8.grid(row=0, column=0, sticky=N+S+E+W)
    label9.grid(row=0, column=1, sticky=N+S+E+W)
    radio_button1_upd.grid(row=1, column=0, sticky=W)
    radio_button2_upd.grid(row=2, column=0, sticky=W)
    radio_button1_ne.grid(row=1, column=1, sticky=W)
    radio_button2_ne.grid(row=2, column=1, sticky=W)
    # Press the <Enter> key to call the event handler
    radio_button1_ne.bind("<Button-1>", button_ne_handler)
    radio_button2_ne.bind("<Button-1>", button_ne_handler)
    radio_button1_upd.bind("<Button-1>", button_upd_handler)
    radio_button2_upd.bind("<Button-1>", button_upd_handler)

    green = Frame(cyan, highlightcolor="green", highlightbackground="green",  highlightthickness=5)
    # place green frame on left on cyan frame
    green.grid(row=0, column=1, stick=N+S+E)
    green.rowconfigure(0, weight=1)
    green.rowconfigure(1)
    green.rowconfigure(2)
    green.columnconfigure(0)
    green.columnconfigure(1)
    label_none = ttk.Label(green, text=" ", font=font.Font(family="Times New Roman", size=10))
    control_baseball = IntVar()
    control_baseball.set(0)
    control_football = IntVar()
    control_football.set(0)
    control_basketball = IntVar()
    control_basketball.set(0)
    control_hockey = IntVar()
    control_hockey.set(0)
    check_button_baseball = ttk.Checkbutton(green, variable=control_baseball, text="Baseball")
    check_button_football = ttk.Checkbutton(green, variable=control_football, text="Football")
    check_button_basketball = ttk.Checkbutton(green, variable=control_basketball, text="Basketball")
    check_button_hockey = ttk.Checkbutton(green, variable=control_hockey, text="Hockey")
    label_none.grid(row=00)
    check_button_baseball.grid(row=1, column=0, stick=W)
    check_button_football.grid(row=2, column=0, stick=W)
    check_button_basketball.grid(row=1, column=1, stick=W)
    check_button_hockey.grid(row=2, column=1, stick=W)
    check_button_baseball.bind("<ButtonRelease-1>", button_check_handler)
    check_button_football.bind("<ButtonRelease-1>", button_check_handler)
    check_button_basketball.bind("<ButtonRelease-1>", button_check_handler)
    check_button_hockey.bind("<ButtonRelease-1>", button_check_handler)

    red = Frame(root, highlightcolor="red", highlightbackground="red", highlightthickness=5)
    red.grid(row=2, column=0, sticky=N + S + E + W)
    red.rowconfigure(0, weight=1)
    red.rowconfigure(1)
    red.columnconfigure(0, weight=1)
    red.columnconfigure(1)
    label10 = ttk.Label(red, text="Other Comments:", font=font.Font(family="Times New Roman", size=12))
    text_command = Text(red, wrap=WORD, height=10, width=50)
    y_scrollbar = ttk.Scrollbar(red, orient=VERTICAL, command=text_command)
    text_command["yscrollcommand"] = y_scrollbar.set
    label10.grid(row=0, sticky=S+W)
    text_command.grid(row=1, column=0, sticky=N+S+E+W)
    y_scrollbar.grid(row=1, column=1, sticky=N+S)
    # Press the <Enter> key to call the event handler
    text_command.bind("<KeyPress-Return>", enter_press_text_handler)

    blue = Frame(root, highlightcolor="blue", highlightbackground="blue", highlightthickness=5)
    blue.grid(row=3, column=0, sticky=N + S + E + W)
    blue.rowconfigure(0, weight=1)
    blue.columnconfigure(0, weight=1)
    blue.columnconfigure(1, weight=1)
    button_submit = ttk.Button(blue, text="Submit")
    button_cancel = ttk.Button(blue, text="Cancel")
    button_submit.grid(row=0, column=0, sticky=N+S+E+W)
    button_cancel.grid(row=0, column=1, sticky=N+S+E+W)
    button_submit.bind_class("TButton", "<ButtonRelease-1>", button_released_handler)
    button_cancel.bind_class("TButton", "<ButtonRelease-1>", button_released_handler)

    root.mainloop()

if __name__ == "__main__":
    main()
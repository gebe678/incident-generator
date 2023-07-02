import tkinter as tk
from tkinter import StringVar
from tkinter import OptionMenu
from config import inputs

# create the main window
window = tk.Tk()

# create the initial drop down menu that will determine the rest of the options
# incident_types = StringVar(window)
# incident_types.set(inputs["inputs"]["incidents"][0])

# # actual incidents menu for the gui
# incident_menu = OptionMenu(window, incident_types, *inputs["inputs"]["incidents"])

# # create dropdown list for operating systems
# os_types = StringVar(window)
# os_types.set(inputs["inputs"]["operating_systems"][0])

# os_menu = OptionMenu(window, os_types, *inputs["inputs"]["operating_systems"])

# # trace - checks to see if the value in the option menues has been changed
# incident_types.trace("w", create_dependent_inputs)
# os_types.trace("w", create_dependent_inputs)

# # show the option menues in the gui
# incident_menu.pack()
# os_menu.pack()

# variables to show to the user
gui_vars = {"var": [], "row": [], "col": []}

# loop through the config options and create the inputs for the ticket
# must update to add types that are added to the config file
for i in inputs["inputs"]:
    input_type = inputs["inputs"][i]["type"]

    if input_type == "OptionMenu":
        options = inputs["inputs"][i]["options"]
        menu_options = StringVar(window)
        menu_options.set(options[0])

        menu = OptionMenu(window, menu_options, *options)

        gui_vars["var"].append(menu)
        gui_vars["row"].append(inputs["inputs"][i]["row"])
        gui_vars["col"].append(inputs["inputs"][i]["column"])

    else:
        print("unknown type")

for var in range(len(gui_vars["var"])):
    gui_vars["var"][var].grid(row = gui_vars["row"][var], column = gui_vars["col"][var])

window.mainloop()
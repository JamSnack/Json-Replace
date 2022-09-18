#made by JamSnack  /(,0,)/ for Dingo :)
#9/17/2022

import json
import tkinter as tk
from tkinter import filedialog

print("Begin program")


#init vars
file_to_change = ""
file_changes = ""
new_file_name = ""


#----FUNCTIONS----
def combine_files(file_to_change, file_changes):
    json_file_to_copy = file_to_change
    json_file_encoding = "utf-8-sig"
    json_file_changes = file_changes
    json_file_changes_encoding = "utf-8-sig"
    new_file_name = entry_new_file.get()

    #correct naming errors
    if (not (".json" in new_file_name)):
        new_file_name = new_file_name + ".json"
    
    #attempting to combine files...
    print("Copying: " + str(json_file_to_copy) + "\n" + "With Changes: " + str(json_file_changes) + "\n")

    with open(json_file_to_copy, "r", encoding = json_file_encoding) as read_content:
        eng_dict = json.load(read_content)

    print("\n\nLoaded file 1")

    with open(json_file_changes, "r", encoding = json_file_changes_encoding) as read_content:
        jap_dict = json.load(read_content)

    print("\n\nLoaded file 2")

    for e in jap_dict:
        if (eng_dict.get(e) != None):
            if (type(eng_dict[e]) is dict):
                for v in eng_dict[e]:
                    if (jap_dict[e].get(v) != None):
                        eng_dict[e][v] = jap_dict[e][v]
            else:
                eng_dict[e] = jap_dict[e]


    new_file = open(new_file_name, mode="w", encoding = "utf-8")
    json.dump(eng_dict, new_file, indent = 4, ensure_ascii = False)
    new_file.close()
    filedialog.askopenfilename()
    print("\n\nCreated new file")



#----TKINTER-----
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 677, height = 5)
canvas1.pack()

#Tkinter functions
def ask_for_file_to_change():
    global file_to_change
    file_to_change = str(filedialog.askopenfilename())
    change_text(t1, file_to_change)
    print("File to Change: " + file_to_change)

def ask_for_file_changes():
    global file_changes
    file_changes = str(filedialog.askopenfilename())
    change_text(t2, file_changes)
    print("File Changes: " + file_changes)

def change_text(text_object, text):
    text_object.config(text = text)

#buttons
button_file_to_change = tk.Button(root, text = "Select JSON File to Change", command = lambda: ask_for_file_to_change())
button_file_changes = tk.Button(root, text = "Select JSON File Changes", command = lambda:ask_for_file_changes())


#input fields
entry_new_file = tk.Entry(root)

# Create label
l = tk.Label(root, text = "JSON Replacer v1.0")
l.config(font =("Courier", 14))
 
# Create an change json button.
b1 = tk.Button(root, text = "Change JSON", command = lambda: combine_files(file_to_change, file_changes))

#Text objects and necessary fields
text_file_to_change = ""
t1 = tk.Label(root, text = "No File Selected")

text_file_changes = ""
t2 = tk.Label(root, text = "No File Selected")

t3 = tk.Label(root, text = "\nEnter New Filename: ")


#we're packing
l.pack()
button_file_to_change.pack()
t1.pack()
button_file_changes.pack()
t2.pack()
t3.pack()
entry_new_file.pack()
b1.pack()

#init mainloop
root.mainloop()
    

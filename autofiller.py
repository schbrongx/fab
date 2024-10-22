import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pyperclip
import json
from custom_ui import custom_yesnocancel
from ui_helper import add_tooltip

# Initialize current_file_path variable
global current_file_path
current_file_path = None

# Clear all rows except the first one, used to reset the data
def neu_datei():
    global current_file_path
    current_file_path = None
    root.title("Neue Datei")
    if len(rows) > 1:
        del rows[1:]
    clear_row(0)
    refresh_table()
    update_status()

# Save current data to a JSON file
def save_file():
    global current_file_path
    if current_file_path:
        save_to_path(current_file_path)
    else:
        save_file_as()

# Save current data to a specific path
def save_to_path(file_path):
    data_to_save = []
    for i, row in enumerate(rows):
        data_to_save.append({
            'position': i + 1,
            'name': row['name'].get(),
            'feldname': row['feldname'].get(),
            'wert': row['wert'].get()
        })
    with open(file_path, 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)
    root.title(f"{file_path}")
    global changes_made
    changes_made = False

# Save current data to a JSON file
def save_file_as():
    global current_file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if file_path:
        current_file_path = file_path
        save_to_path(file_path)

# Load data from a JSON file and populate the table
def load_file():
    global current_file_path
    file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r') as json_file:
                rows.clear()
                data_loaded = json.load(json_file)
                # Check if the loaded data matches the expected format
                if isinstance(data_loaded, list) and all(isinstance(entry, dict) and 'position' in entry and 'name' in entry and 'feldname' in entry and 'wert' in entry for entry in data_loaded):
                    rows.clear()
                    for entry in data_loaded:
                        new_row = create_row()
                        new_row['name'].set(entry['name'])
                        new_row['feldname'].set(entry['feldname'])
                        new_row['wert'].set(entry['wert'])
                        rows.append(new_row)
                    refresh_table()
                    update_status()
                    current_file_path = file_path
                    root.title(f"{file_path}")
                    global changes_made
                    changes_made = False
                else:
                    messagebox.showerror("Fehler", "Die Datei hat nicht das erwartete Format.")
        except Exception as e:
            messagebox.showerror("Fehler", f"Die Datei konnte nicht geladen werden: {str(e)}")

# Quit the application
def quit():
    if changes_made:
        answer = custom_yesnocancel(root, "Ungespeicherte Änderungen", "Möchten Sie die Änderungen vor dem Schliessen speichern?")
        if answer is None:
            return  # Cancel, do not quit
        elif answer:
            save_file()
    root.quit()

# Create a new row with empty values
def create_row():
    return {
        'name': tk.StringVar(),
        'feldname': tk.StringVar(),
        'wert': tk.StringVar(),
        'widgets': {}
    }

# Add a new row at the specified index
def add_row(index):
    rows.insert(index, create_row())
    refresh_table()
    update_status()
    global changes_made
    changes_made = True

# Delete a row at the specified index, ensure at least one row remains
def delete_row(index):
    if len(rows) > 1:
        del rows[index]
        refresh_table()
        update_status()
        global changes_made
        changes_made = True

# Clear the contents of a specific row
def clear_row(index):
    rows[index]['name'].set("")
    rows[index]['feldname'].set("")
    rows[index]['wert'].set("")
    global changes_made
    changes_made = True

# Move a row up in the list
def move_row_up(index):
    if index > 0:
        rows[index], rows[index-1] = rows[index-1], rows[index]
        refresh_table()
        global changes_made
        changes_made = True

# Move a row down in the list
def move_row_down(index):
    if index < len(rows) - 1:
        rows[index], rows[index+1] = rows[index+1], rows[index]
        refresh_table()
        global changes_made
        changes_made = True


# Function to generate JavaScript bookmarklet
def generate_bookmarklet():
    # Start of the bookmarklet JavaScript code
    bookmarklet_code = "javascript:(function(){var d=document,n=d.getElementsByName.bind(d);"

    # Iterate through each row and add corresponding JavaScript code for form filling
    for row in rows:
        feldname = row['feldname'].get().strip()
        wert = row['wert'].get().strip()
        if feldname:  # Only add code if feldname is not empty
            bookmarklet_code += f"n('{feldname}')[0].value=\"{wert}\";"

    # End of the bookmarklet JavaScript code
    bookmarklet_code += "})();"

    # Update the bookmarklet entry field with the generated code
    bookmarklet_entry.delete(0, tk.END)
    bookmarklet_entry.insert(0, bookmarklet_code)


# Refresh the table UI, recreate all widgets based on the current data
def refresh_table():
    global bookmarklet_entry  # Declare bookmarklet_entry as global to use it in other functions

    # Remove all existing widgets from the display area
    for widget in displayarea.winfo_children():
        widget.destroy()

    # Add the bookmarklet row at the top of the display area
    generate_button = tk.Button(displayarea, text="Bookmarklet generieren", command=generate_bookmarklet)
    generate_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    add_tooltip(generate_button, "Generiere ein Bookmarklet-Skript, das du verwenden kannst.")

    def copy_bookmarklet():
        pyperclip.copy(bookmarklet_entry.get())
        copy_button.config(text="✓", fg="green")
        displayarea.after(3000, lambda: copy_button.config(text="📋", fg="black"))

    copy_button = tk.Button(displayarea, text="📋", command=copy_bookmarklet)
    copy_button.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    add_tooltip(copy_button, "Kopiere den Bookmarklet-Code in die Zwischenablage.")

    bookmarklet_entry = tk.Entry(displayarea)
    bookmarklet_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
    displayarea.grid_columnconfigure(2, weight=1)  # Make the text field grow with the window

    # Add column headers
    tk.Label(displayarea, text="Nr.", font=("Helvetica", 10, "bold"), bd=1, relief="solid").grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    tk.Label(displayarea, text="Name", font=("Helvetica", 10, "bold"), bd=1, relief="solid").grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    tk.Label(displayarea, text="Feldname", font=("Helvetica", 10, "bold"), bd=1, relief="solid").grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
    tk.Label(displayarea, text="Wert", font=("Helvetica", 10, "bold"), bd=1, relief="solid").grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
    displayarea.grid_columnconfigure(3, weight=1)  # Column "Wert" will grow with the window

    # Recreate widgets for each row
    for i, row in enumerate(rows):
        # Row number
        tk.Label(displayarea, text=str(i + 1), font=("Helvetica", 10, "bold"), bd=1, relief="solid").grid(row=i + 2, column=0, padx=5, pady=5, sticky="nsew")

        # Input fields
        tk.Entry(displayarea, textvariable=row['name'], bd=1, relief="solid").grid(row=i + 2, column=1, padx=5, pady=5, sticky="nsew")
        tk.Entry(displayarea, textvariable=row['feldname'], bd=1, relief="solid").grid(row=i + 2, column=2, padx=5, pady=5, sticky="nsew")
        tk.Entry(displayarea, textvariable=row['wert'], bd=1, relief="solid").grid(row=i + 2, column=3, padx=5, pady=5, sticky="nsew")

        # Buttons for row actions
        clear_button = tk.Button(displayarea, text="x", command=lambda i=i: clear_row(i), bd=1, relief="solid")
        clear_button.grid(row=i + 2, column=4, padx=5, pady=5, sticky="nsew")
        add_tooltip(clear_button, "Lösche den Inhalt dieser Zeile.")

        delete_button = tk.Button(displayarea, text="-", command=lambda i=i: delete_row(i), state=(tk.NORMAL if len(rows) > 1 else tk.DISABLED), bd=1, relief="solid")
        delete_button.grid(row=i + 2, column=5, padx=5, pady=5, sticky="nsew")
        add_tooltip(delete_button, "Lösche diese Zeile.")

        add_button = tk.Button(displayarea, text="+", command=lambda i=i: add_row(i + 1), bd=1, relief="solid")
        add_button.grid(row=i + 2, column=6, padx=5, pady=5, sticky="nsew")
        add_tooltip(add_button, "Füge eine neue Zeile nach dieser hinzu.")

        up_button = tk.Button(displayarea, text="↑", command=lambda i=i: move_row_up(i), state=(tk.NORMAL if i > 0 else tk.DISABLED), bd=1, relief="solid")
        up_button.grid(row=i + 2, column=7, padx=5, pady=5, sticky="nsew")
        add_tooltip(up_button, "Verschiebe diese Zeile nach oben.")

        down_button = tk.Button(displayarea, text="↓", command=lambda i=i: move_row_down(i), state=(tk.NORMAL if i < len(rows) - 1 else tk.DISABLED), bd=1, relief="solid")
        down_button.grid(row=i + 2, column=8, padx=5, pady=5, sticky="nsew")
        add_tooltip(down_button, "Verschiebe diese Zeile nach unten.")


# Open a new window for the bookmarklet, used to display a JavaScript snippet
def open_bookmarklet_window():
    bookmarklet_window = tk.Toplevel(root)
    bookmarklet_window.grab_set()  # Block the main window until this one is closed
    bookmarklet_window.title("Bookmarklet für Formularnamen")
    bookmarklet_window.geometry("500x300")
    bookmarklet_window.resizable(False, False)  # Fix window size

    # Information label explaining the purpose of the bookmarklet
    info_label = tk.Label(bookmarklet_window, text="Dieses Bookmarklet kann man im Browser verwenden um die Feldnamen von Formularen auf Internetseiten einzublenden. Diese Feldnamen benötigt das Programm zum automatischen Ausfüllen.", wraplength=480, justify="left")
    info_label.pack(pady=10, padx=10)

    # Copy the JavaScript code to the clipboard
    def copy_to_clipboard():
        pyperclip.copy(bookmarklet_code)
        copy_button.config(text="✓", fg="green")
        bookmarklet_window.after(3000, lambda: copy_button.config(text="📋", fg="black"))

    # Frame for the copy button
    copy_frame = tk.Frame(bookmarklet_window)
    copy_frame.pack(pady=5, anchor="w", padx=10)

    copy_button = tk.Button(copy_frame, text="📋", command=copy_to_clipboard)
    copy_button.pack(side=tk.LEFT)
    add_tooltip(copy_button, "Kopiere den JavaScript-Code in die Zwischenablage.")

    copy_label = tk.Label(copy_frame, text="Inhalt in die Zwischenablage kopieren")
    copy_label.pack(side=tk.LEFT, padx=5)

    # Text area with the JavaScript code
    bookmarklet_code = "javascript:(function(){var existingLabels=document.querySelectorAll('.custom-field-label');if(existingLabels.length){existingLabels.forEach(function(label){label.remove();});}else{var inputs=document.querySelectorAll('input, select, textarea');inputs.forEach(function(input){var label=document.createElement('span');label.className='custom-field-label';label.style.cssText='font-size:12px;color:red;background-color:yellow;position:absolute;z-index:9999;padding:2px;margin-bottom:5px;';var labelContent=input.name?'Name: '+input.name:'No Name Attribute';if(input.type==='radio'||input.type==='checkbox'){labelContent+=', Wert: '+input.value;label.style.backgroundColor='green';label.style.color='white';}label.innerHTML=labelContent;var rect=input.getBoundingClientRect();label.style.top=(window.scrollY+rect.top-10)+'px';label.style.left=(window.scrollX+rect.left)+'px';document.body.appendChild(label);});}})();"
    textarea = tk.Text(bookmarklet_window, wrap=tk.WORD, height=3, width=60)
    textarea.insert(tk.END, bookmarklet_code)
    textarea.config(state=tk.DISABLED)
    textarea.pack(padx=10, pady=(5, 0), side=tk.TOP, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(bookmarklet_window, command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y, in_=textarea)

    # Button to close the bookmarklet window
    close_button = tk.Button(bookmarklet_window, text="Schließen", command=bookmarklet_window.destroy)
    close_button.pack(pady=10)
    add_tooltip(close_button, "Schließe dieses Fenster.")


# Create the main window
root = tk.Tk()
root.title("Hauptfenster")
root.geometry("600x500")

# Create the menu bar
menubar = tk.Menu(root)

# "File" menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Neu", command=neu_datei)
file_menu.add_command(label="Speichern", command=save_file)
file_menu.add_command(label="Speichern unter ...", command=save_file_as)
file_menu.add_command(label="Laden", command=load_file)
file_menu.add_separator()
file_menu.add_command(label="Beenden", command=quit)

menubar.add_cascade(label="Datei", menu=file_menu)

# "Help" menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Bookmarklet für Formularnamen", command=open_bookmarklet_window)

menubar.add_cascade(label="Hilfe", menu=help_menu)

# Add the menu bar to the main window
root.config(menu=menubar)

# Display area for rows
displayarea = tk.Frame(root, bg="lightgray")
displayarea.pack(fill=tk.BOTH, expand=True)

# Create initial row
rows = [create_row()]
refresh_table()

# Create status bar to display number of form fields
status_label = tk.Label(root, text=f"Anz. Formularfelder: {len(rows)}", anchor="w")
status_label.pack(side=tk.BOTTOM, fill=tk.X)

# Function to update the status bar with the current number of rows
def update_status():
    status_label.config(text=f"Anz. Formularfelder: {len(rows)}")

# Track changes to prompt save on exit
changes_made = False

# Start the main loop
root.protocol("WM_DELETE_WINDOW", quit)
root.mainloop()

# custom_ui.py
import tkinter as tk

# Custom yesnocancel dialog with German buttons
def custom_yesnocancel(root, title, message):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry("300x150")
    dialog.transient(root)
    dialog.grab_set()

    tk.Label(dialog, text=message, wraplength=250).pack(pady=20)

    result = {'value': None}

    def on_yes():
        result['value'] = True
        dialog.destroy()

    def on_no():
        result['value'] = False
        dialog.destroy()

    def on_cancel():
        result['value'] = None
        dialog.destroy()

    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)

    yes_button = tk.Button(button_frame, text="Ja", command=on_yes, width=10)
    yes_button.grid(row=0, column=0, padx=5)

    no_button = tk.Button(button_frame, text="Nein", command=on_no, width=10)
    no_button.grid(row=0, column=1, padx=5)

    cancel_button = tk.Button(button_frame, text="Abbrechen", command=on_cancel, width=10)
    cancel_button.grid(row=0, column=2, padx=5)

    dialog.wait_window()
    return result['value']
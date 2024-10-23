# ui_helper.py
import os
import sys
import tkinter as tk

# Helper function to add tooltip to buttons
def add_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.withdraw()
    tooltip.overrideredirect(True)
    label = tk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1, font=("Helvetica", 10))
    label.pack()

    def enter(event):
        x, y, _, _ = widget.bbox("insert")
        x += widget.winfo_rootx() + 25
        y += widget.winfo_rooty() + 25
        tooltip.geometry(f"+{x}+{y}")
        tooltip.deiconify()

    def leave(event):
        tooltip.withdraw()

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller compiled exe """
    if hasattr(sys, '_MEIPASS'):
        # Wenn wir in einer PyInstaller-Build laufen, dann _MEIPASS benutzen
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Andernfalls einfach den relativen Pfad verwenden
        return os.path.join(os.path.abspath("."), relative_path)
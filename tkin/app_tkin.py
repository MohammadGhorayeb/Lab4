"""
app_tkin.py

This module serves as the entry point for the School Management System application.

Classes:
    None

Functions:
    main() -> None:
        Initializes and runs the Tkinter application.
"""

import tkinter as tk
from gui_tkin import SchoolManagementSystem  # Import the main GUI class from gui.py

def main():
    root = tk.Tk()  # Create the root window
    app = SchoolManagementSystem(root)  # Initialize the SchoolManagementSystem class
    root.mainloop()  # Start the Tkinter main loop

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames.chat import Chat

COLOR_LIGHT_BACKGROUND_1 = "#fff"
COLOR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOR_LIGHT_BACKGROUND_3 = "#e3e5e8"

COLOR_LIGHT_TEXT = "#aaa"

COLOR_BUTTON_NORMAL = "#5fba7d"
COLOR_BUTTON_ACTIVE = "#58c77c"
COLOR_BUTTON_PRESSED = "#44e378"


class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1200x500")
        self.minsize(800, 500)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(
            self,
            background=COLOR_LIGHT_BACKGROUND_1,
            style="Messages.TFrame",
        )

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")


if __name__ == "__main__":
    root = Messenger()
    font.nametofont("TkDefaultFont").configure(size=14)
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Messages.TFrame", background=COLOR_LIGHT_BACKGROUND_3)
    style.configure("Controls.TFrame", background=COLOR_LIGHT_BACKGROUND_2)
    style.configure("SendButton.TButton", borderwidth=0, background=COLOR_BUTTON_NORMAL)
    style.map(
        "SendButton.TButton",
        background=[("pressed", COLOR_BUTTON_PRESSED), ("active", COLOR_BUTTON_ACTIVE)],
    )
    style.configure(
        "FetchButton.TButton", background=COLOR_LIGHT_BACKGROUND_1, borderwidth=0
    )
    style.configure(
        "Time.TLabel",
        padding=5,
        background=COLOR_LIGHT_BACKGROUND_1,
        foreground=COLOR_LIGHT_TEXT,
        font=8,
    )
    root.mainloop()

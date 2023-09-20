from tkinter import Tk, Frame, Label, Toplevel, Button

FONT = ("Arial", 20)
HBG = "#EBc0cb"


class App(Tk):
    def __init__(
        self, title: str, width: int = 800, height: int = 600, resizable: bool = True
    ) -> None:
        super().__init__()

        self.resizable(resizable, resizable)
        self.geometry(f"{width}x{height}")
        self.title(title)

        # shortcuts
        self.bind("<q>", lambda _: self.destroy())
        self.bind("<F1>", lambda _: HelpNAbout(self))

    def rebinder(self):
        ...


class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")

        display = Label(self, bg="white", font=FONT)
        display.pack()
        self.display = display

        self.set_display("Press N to start the game.")
        parent.bind("<n>", lambda _: self.update_display("Started the game."))

        # Managing inputs.
        for i in range(10):
            parent.bind(f"{i}", lambda a: print("->", a.char))
            parent.bind(f"<KP_{i}>", lambda a: print("->", a.char))
        parent.bind("<Return>", lambda _: print("You pressed Enter"))
        parent.bind("<KP_Enter>", lambda _: print("You pressed Enter"))

    def set_display(self, to: str):
        self.display.config(text=to)

    def update_display(self, to: str):
        self.display.config(text=to)


class Settings(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="blue")


class HelpNAbout(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent, bg=HBG)

        width = 430
        height = 580
        midx = (self.winfo_screenwidth() - width) // 2
        midy = (self.winfo_screenheight() - height) // 2

        self.transient(parent)
        self.wait_visibility()  # Fixes softlock, which happens when grab_set fails
        self.grab_set()
        self.title("Mathrain help")
        self.geometry(f"{width}x{height}+{midx}+{midy}")
        self.resizable(0, 0)

        # About part
        Label(self, text="What is mathrain?", bg=HBG, font=(FONT[0], 30)).pack(
            pady=(15, 10)
        )
        Label(
            self, text="It is the math trainer, aka math rain.", bg=HBG, font=FONT
        ).pack()
        Label(
            self,
            text="Solve given math problems and\nsee how fast you can do that.",
            bg=HBG,
            font=FONT,
        ).pack(pady=2)

        # Help part
        Label(self, text="Small help note:", bg=HBG, font=(FONT[0], 30)).pack(
            pady=(60, 10)
        )
        htxt = (
            "1. Press Q to close windows.\n"
            "2. To input values use numpad,\nnumbers or custom bindings.\n"
            "3. To confirm use Enter, Spacebar\nor custom key"
        )
        Label(
            self,
            text=htxt,
            bg=HBG,
            font=FONT,
        ).pack()

        # Creator
        me = Button(
            self,
            bg=HBG,
            borderwidth=0,
            relief="sunken",
            highlightcolor=HBG,
            highlightbackground=HBG,
            activebackground=HBG,
            activeforeground="blue",
            text="Made by: Boiiterra.",
            font=FONT + ("underline",),
            command=lambda: print("Button pressed"),
            cursor="hand1",
        )
        me.pack(side="bottom", pady=10)

        self.bind("<q>", lambda _: self.destroy())


if __name__ == "__main__":
    app = App("mathrain", resizable=False)

    Main(app).pack()

    app.mainloop()

import tkinter as tk


class SlideShow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frames = []
        self.current_frame = 0
        self.create_frames()

    def create_frames(self):
        texts = [
            "MWAHAHAHA! I've hacked your computer. Welcome to #DevFest2023, LeetCode Mastery.",
            "In order to stop me from hacking your computer, you must complete the following tasks either by yourself or in a group. Please, using your phone or exiting the application, go to the following links. You will need to (try to) complete the following tasks.",
            "https://shorturl.at/FHU28",
            "https://shorturl.at/wyNP6",
            "https://shorturl.at/otwRZ",
            "If you finished all of the tasks (or atleast tried them), you win, I'll give you access to your computer back. Please exit the application and continue with the workshop!",
        ]
        for text in texts:
            frame = tk.Frame(self)
            label = tk.Label(
                frame,
                text=text,
                font=("Courier", 24),
                wraplength=self.winfo_screenwidth() * 0.8,
            )
            label.pack(side="top", fill="both", expand=True)
            self.frames.append(frame)

        self.btn_prev = tk.Button(
            self, text="←", command=self.prev_frame, font=("Courier", 24)
        )
        self.btn_next = tk.Button(
            self, text="→", command=self.next_frame, font=("Courier", 24)
        )
        self.btn_prev.pack(side="left", padx=20, pady=20)
        self.btn_next.pack(side="right", padx=20, pady=20)

        self.show_frame()

    def show_frame(self):
        for frame in self.frames:
            frame.pack_forget()
        self.frames[self.current_frame].pack(fill="both", expand=True)
        self.update_buttons()

    def next_frame(self):
        self.current_frame = min(self.current_frame + 1, len(self.frames) - 1)
        self.show_frame()

    def prev_frame(self):
        self.current_frame = max(self.current_frame - 1, 0)
        self.show_frame()

    def update_buttons(self):
        self.btn_prev["state"] = "disabled" if self.current_frame == 0 else "normal"
        self.btn_next["state"] = (
            "disabled" if self.current_frame == len(self.frames) - 1 else "normal"
        )

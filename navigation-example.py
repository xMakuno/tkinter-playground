import tkinter as tk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set window size to 60% of the screen dimensions
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)

        # Calculate position to center the window
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2

        # Set dynamic geometry
        self.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.title("Dynamic Multi-View Tkinter App")

        # Create frames for each view
        self.frames = {}
        for F in (HomePage, PageOne, PageTwo):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame(HomePage)

    def show_frame(self, frame_class):
        """Display the given frame."""
        frame = self.frames[frame_class]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Home Page", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Go to Page 1", 
                  command=lambda: controller.show_frame(PageOne)).pack()
        tk.Button(self, text="Go to Page 2", 
                  command=lambda: controller.show_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Page 1", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Home", 
                  command=lambda: controller.show_frame(HomePage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Page 2", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Back to Home", 
                  command=lambda: controller.show_frame(HomePage)).pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

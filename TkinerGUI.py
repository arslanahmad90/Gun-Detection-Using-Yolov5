from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import subprocess

class ImageViewer:
    def __init__(self):
        self.root = Tk()

        self.label = Label(self.root)
        self.label.pack(expand=True)

        self.button = Button(self.root, text="Open Image", command=self.open_image)
        self.button.pack(pady=10)

        self.root.title("Image Viewer")
        self.root.geometry("600x440")
        self.root.resizable(False, False)

        self.root.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.label.config(width=self.root.winfo_width(), height=self.root.winfo_height() - 30)
        self.button.place(x=self.root.winfo_width() // 2 - 50, y=self.root.winfo_height() - 30)

    def open_image(self):
        file_path = filedialog.askopenfilename(title="Select Image File",
                                                filetypes=(("Images", "*.png;*.xpm;*.jpg;*.bmp;*.gif"), ("All files", "*.*")))
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo
        if file_path:
            print("Selected file:", file_path)
            script = f"python detect.py --source \"{file_path}\" --weights last.pt"
            print("Script:", script)

            try:
                subprocess.call(script, shell=True)
                image = Image.open("Temp.png")
                photo = ImageTk.PhotoImage(image)
                self.label.config(image=photo)
                self.label.image = photo
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()


viewer = ImageViewer()
viewer.run()

from PIL import ImageTk, Image
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar
from threading import Thread
import rename
from queue import Queue

class GCEApp:
    # Makes the GUI
    def __init__(self, master):
        self.master = master
        master.title("GCE Rename GUI")
        master.resizable(False, False)

        # Load Images
        self.image = Image.open("background.png")
        self.image2 = Image.open("coin.png")

        # Create Window icon
        self.icon = ImageTk.PhotoImage(self.image2)
        master.iconphoto(False, self.icon)

        # Calculate image dimensions while maintaining the aspect ratio
        self.window_width = 350
        self.window_height = 310
        image_width, image_height = self.image.size
        aspect_ratio = min(self.window_width / image_width, self.window_height / image_height)
        new_width = int(image_width * aspect_ratio)
        new_height = int(image_height * aspect_ratio)
        self.image = self.image.resize((new_width, new_height), Image.BICUBIC)
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a canvas
        self.canvas = tk.Canvas(master, width=self.window_width, height=self.window_height)
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=(2, 1))
        self.canvas.create_image(self.window_width // 2, self.window_height // 2, anchor=tk.CENTER, image=self.photo)

        # Create a label
        self.label = tk.Label(master, text="Enter the start number:")
        self.label.grid(row=2, column=0, padx=10, pady=7)

        # Create an entry field
        self.entry = tk.Entry(master, width=25)
        self.entry.grid(row=2, column=1, padx=10, pady=7)

        # Create a rename button
        self.button = tk.Button(master, text="Rename Files", command=self.execute_rename, width=12)
        self.button.grid(row=3, column=0, columnspan=1, padx=2, pady=(5 , 15))
        
        # Create a change CSV button
        self.button = tk.Button(master, text="Update CSV", command=self.execute_csv, width=12, state='disabled')
        self.button.grid(row=3, column=1, columnspan=1, padx=2, pady=(5, 15))
        
        # Create a progress bar
        self.progress_bar = Progressbar(master, length=335, mode='determinate')
        self.progress_bar.grid(row=1, column=0, columnspan=2, padx=10, pady=(2, 7))

    def execute_rename(self):
        start_number = self.entry.get()
        try:
            start_number = int(start_number)

            folder_path = filedialog.askdirectory()  # Change to the folder containing images to rename
            files = rename.get_file_list(folder_path)
            total_files = len(files)

            queue = Queue()
            thread = Thread(target=self.rename_files, args=(folder_path, start_number, files, queue))
            thread.start()
            self.update_progress_bar(total_files, queue)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter an integer.")

    def rename_files(self, folder_path, start_number, files, queue):
        total_files = rename.rename_files(folder_path, start_number, files)

        for _ in range(total_files):
            queue.put(1)  # Increment progress

        queue.put(0)  # Indicate completion

    def execute_csv(self):
        row_number = (int(self.entry.get())+1) 
        column_number = 13
        column_item_id = 4
        try:
            self.print(row_number)
        except:
            self.print(column_number, column_item_id)
            
    
    def update_progress_bar(self, total_files, queue):
        progress = 0
        while progress < total_files:
            progress += queue.get()
            self.progress_bar["value"] = progress
            self.master.update()

        self.progress_bar["value"] = total_files
        self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = GCEApp(root)
    root.mainloop()

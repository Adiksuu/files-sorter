import os
import shutil
import tkinter as tk
from tkinter import ttk
from colorama import Fore

def sort_images():
    # Create the images folder
    os.makedirs("images", exist_ok=True)
    files = [filename for filename in os.listdir() if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    # Sort the list of files
    files.sort()
    # Move and rename files in the images folder
    for i, filename in enumerate(files):
        # Get the file extension
        ext = os.path.splitext(filename)[1]
        # Move the file to the images folder
        new_filename = f"image-{i+1}{ext}"
        shutil.move(filename, os.path.join("images", new_filename))
    print(Fore.YELLOW + f"Sorted {len(files)} files in the images folder")

def sort_videos():
    # Create the videos folder
    os.makedirs("videos", exist_ok=True)
    files = [filename for filename in os.listdir() if filename.lower().endswith((".mp4", ".avi", ".mkv", ".mov"))]
    # Sort the list of files
    files.sort()
    # Move and rename files in the videos folder
    for i, filename in enumerate(files):
        # Get the file extension
        ext = os.path.splitext(filename)[1]
        # Move the file to the videos folder
        new_filename = f"video-{i+1}{ext}"
        shutil.move(filename, os.path.join("videos", new_filename))
    print(Fore.YELLOW + f"Sorted {len(files)} files in the videos folder")

def sort_all():
    sort_images()
    sort_videos()

# Create the main window
root = tk.Tk()
root.title("File Sorter")
root.minsize(500, 200)
root.maxsize(800, 200)
root.configure(bg="white")

# Create the frame for the radio buttons
frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# Create the radio buttons
file_choice = tk.IntVar(value=1)
image_button = ttk.Button(frame, text="Sort images", style="TButton", command=sort_images)
image_button.pack(fill="both", padx=10, pady=5)
video_button = ttk.Button(frame, text="Sort videos", style="TButton", command=sort_videos)
video_button.pack(fill="both", padx=10, pady=5)
all_button = ttk.Button(frame, text="Sort all", style="TButton", command=sort_all)
all_button.pack(fill="both", padx=10, pady=5)

# Add padding to the buttons
for child in frame.winfo_children():
    child.configure(padding=5)

# Run the main loop
root.mainloop()

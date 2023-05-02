import os
import shutil
import tkinter as tk
from tkinter import filedialog
from extensions import extensions
from pathlib import Path
from collections import defaultdict
import tkinter.messagebox as messagebox

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Prompt the user to select the directory they want to organize
path = Path(filedialog.askdirectory(title="Select Directory to Organize"))
if not path:
    print("No directory selected.")
    exit()

# Create the folders if they do not already exist
counts = defaultdict(int)
for folder in extensions.values():
    folder_path = path / folder
    if not folder_path.exists():
        folder_path.mkdir()
    counts[folder] = 0

# Loop through all the files and subdirectories in the directory
for root, dirs, files in os.walk(path):
    for filename in files:
        file_path = Path(root) / filename
        if file_path.is_file():
            file_extension = file_path.suffix.lower()
            if file_extension in extensions:
                destination_folder = path / extensions[file_extension]

                # Create a new name by appending a number to the filename until it's unique
                new_file_name = filename
                i = 1
                while (destination_folder / new_file_name).exists():
                    name, ext = os.path.splitext(filename)
                    new_file_name = f"{name}_{i}{ext}"
                    i += 1

                # Remove all instances of the pattern "_1" from the filename
                new_file_name = new_file_name.replace("_1", "")

                # Move the file to the destination folder
                try:
                    shutil.move(file_path, destination_folder / new_file_name)
                except Exception as e:
                    print(f"Error moving file {file_path}: {e}")

                # Increment the count for the destination folder
                counts[extensions[file_extension]] += 1

            # Create new folder for unknown file extension
            else:
                folder_name = input(f"Enter folder name for files with extension '{file_extension}': ")
                extensions[file_extension] = folder_name
                folder_path = path / folder_name
                if not folder_path.exists():
                    folder_path.mkdir()
                try:
                    shutil.move(file_path, folder_path / filename)
                except Exception as e:
                    print(f"Error moving file {file_path}: {e}")
                counts[folder_name] += 1

# Display the number of files moved to each folder
for folder, count in counts.items():
    print(f"{count} files were moved to the {folder} folder.")

# Remove empty directories
for root, dirs, files in os.walk(path, topdown=False):
    for dir in dirs:
        dir_path = Path(root) / dir
        if not any(dir_path.iterdir()):
            dir_path.rmdir()

# Notify the user that the organization process is complete
print("Organizing files in directory is complete!")

if messagebox.askyesno("Organize Files", "Do you want to open the destination folder?"):
    os.startfile(path)
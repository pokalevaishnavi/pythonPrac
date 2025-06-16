import os

# Get current working directory
print(os.getcwd())  # Returns the current directory (like 'C:\\Users\\User\\folder')

# Change current working directory
os.chdir('..')  # Goes one level up in the directory tree

# Change back to original directory
os.chdir("file_IO")

# List files and directories in a given path
print(os.listdir())  # Lists all files/folders in the current directory

# Make a new directory
os.mkdir('new_folder')  # Creates a single directory named 'new_folder'

# Make nested directories
os.makedirs('parent_folder/child_folder')  # Creates both folders at once

# Remove a single directory (only if empty)
os.rmdir('new_folder')  # Deletes 'new_folder'

# Remove nested directories
os.removedirs('parent_folder/child_folder')  # Deletes both folders if they’re empty

# Rename a file or directory
os.rename('old_name.txt', 'new_name.txt')  # Renames a file or directory

# Get file status
print(os.stat('new_name.txt'))  # Returns info like size, modification time, etc.

# Walk through directory tree
for dirpath, dirnames, filenames in os.walk('.'):
    print(f"Directory: {dirpath}")
    print(f"Subdirectories: {dirnames}")
    print(f"Files: {filenames}")

# Get environment variable
print(os.environ.get('PATH'))  # Gets the PATH environment variable

# Set environment variable
os.environ['MY_VAR'] = '123'  # Sets an environment variable (temporary)

# Execute a system command
os.system('echo Hello')  # Executes a command like in terminal/cmd

# Get absolute path
print(os.path.abspath('new_name.txt'))  # Converts a relative path to absolute

# Check if a path exists
print(os.path.exists('new_name.txt'))  # Returns True if file/folder exists

# Check if a path is a file
print(os.path.isfile('new_name.txt'))  # Returns True if it's a file

# Check if a path is a directory
print(os.path.isdir('parent_folder'))  # Returns True if it's a directory

# Join paths in an OS-safe way
path = os.path.join('folder', 'subfolder', 'file.txt')  # Joins parts using correct separators

# Split path into (head, tail)
print(os.path.split(path))  # Splits 'folder/subfolder/file.txt' into ('folder/subfolder', 'file.txt')

# Split file into name and extension
print(os.path.splitext('file.txt'))  # Returns ('file', '.txt')

# Get file size
print(os.path.getsize('new_name.txt'))  # Returns size in bytes

# Get last modified time
print(os.path.getmtime('new_name.txt'))  # Returns timestamp of last modification

# Start a file with its default app (Windows only)
# os.startfile('new_name.txt')  # Opens the file like double-clicking (Windows only)


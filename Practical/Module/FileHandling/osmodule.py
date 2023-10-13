# import os

# # Get the name of the operating system
# print("Operating System:", os.name)

# # Get the current working directory
# print("Current Directory:", os.getcwd())

# # List files and directories in the current directory
# print("Files and Directories in Current Directory:")
# for item in os.listdir():
#     print(item)

# import os
# # Create a new directory
# os.mkdir("my_directory")

# # Rename a directory
# os.rename("my_directory", "new_directory")
# for item in os.listdir():
#     print(item)

# # Remove a directory
# print("\nAfter removing directory")
# os.rmdir("new_directory")
# for item in os.listdir():
#     print(item)

import os

# Check if a file exists
if os.path.exists("my_file.txt"):
    print("File exists")
    os.remove("my_file.txt")  # Delete a file
else:
    print("File does not exist")


# Rename a file
os.rename("old_file.txt", "new_file.txt")

# import os

# # Join paths using os.path.join for platform-independent path handling
# path = os.path.join("my_directory", "my_file.txt")

# # Split a path into its directory and file components
# directory, filename = os.path.split(path)

# # Get the file extension
# file_extension = os.path.splitext(filename)[1]


# import os

# # Get the value of an environment variable
# home_dir = os.getenv("HOME")

# # Set an environment variable (note: this affects the current session only)
# os.environ["MY_VARIABLE"] = "my_value"

# # Remove an environment variable (note: this affects the current session only)
# del os.environ["MY_VARIABLE"]


# import os

# # Execute a shell command and capture the output
# result = os.popen("ls -l").read()
# print(result)

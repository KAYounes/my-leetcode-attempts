import os
import re
import sys

def rename_file(new_name, current_file=None):
    if(current_file is None): raise TypeError("current_file not passed", current_file)
    if not (os.path.exists(current_file)): raise TypeError("current_file is not a valid path to a file", current_file)

    base_name = os.path.basename(current_file)

    if not (new_name.endswith(".py")):
        new_name += '.py'

    # Sanitize the new name
    sanitized_name = re.sub(r'([^a-zA-Z0-9]+)(?=.*\.py)', "_", new_name)

    # If the sanitized name is empty after sanitizing, exit
    if not sanitized_name:
        print("Invalid file name. Please provide a valid name.")
        return

    # Construct the new file path
    directory = os.path.dirname(current_file)
    new_file_path = os.path.join(directory, sanitized_name)

    # Check if the current file name is already equal to the new name
    if base_name == sanitized_name:
        # print("File name is already equal to the new name.")
        return
    
    # Rename the file
    os.rename(current_file, new_file_path)

    # If the sanitized name is different from the provided new name, print a message
    if sanitized_name != new_name:
        print(f"Name modified to be valid file\n\t\"{new_name}\" => \"{sanitized_name}\"")

    print(f"File renamed from {os.path.basename(current_file)} to {sanitized_name}")

# if __name__ == "__main__":
#     new_name = input("Enter the new name for the file: ")
#     rename_file(new_name)
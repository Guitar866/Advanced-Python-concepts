import os
import shutil

folder = "files"

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    # Check whether it is a file
    if os.path.isfile(file_path):

        # Get the file extension
        extension = os.path.splitext(file)[1].lower()

        # Remove the dot from extension
        extension = extension[1:]

        # If file has no extension
        if extension == "":
            folder_name = "Others"
        else:
            folder_name = extension.upper()

        # Create folder if it does not exist
        destination = os.path.join(folder, folder_name)

        if not os.path.exists(destination):
            os.mkdir(destination)

        # Move the file
        shutil.move(file_path, destination)

print("Files arranged successfully!")
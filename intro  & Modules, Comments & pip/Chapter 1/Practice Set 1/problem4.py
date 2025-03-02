import os

def list_directory_contents(directory_path):
    # __define-ocg__ - This function lists all files and directories in the specified path
    try:
        # Get the list of entries in the directory
        entries = os.listdir(directory_path)
        # Iterate through the entries
        for entry in entries:
            # Construct the full path
            full_path = os.path.join(directory_path, entry)
            # Check if it's a file or directory
            if os.path.isdir(full_path):
                print(f"Directory: {entry}")
            else:
                print(f"File: {entry}")
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {directory_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '/1'  # Replace with your directory path
list_directory_contents(directory_path)
import os

def print_file_structure(root_dir, indent=''):
    """
    Function to print the file structure recursively.
    """
    # List all files and directories in the root directory
    items = os.listdir(root_dir)

    # Iterate through each item
    for item in items:
        # Get the full path of the item
        item_path = os.path.join(root_dir, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Print the directory name with proper indentation
            print(indent + item + '/')
            # Recursively call the function for the directory
            print_file_structure(item_path, indent + '  ')
        else:
            # Print the file name
            print(indent + item)

# Replace 'path_to_your_flask_app' with the root directory of your Flask application
root_directory = 'app/'

# Call the function with the root directory
print_file_structure(root_directory)

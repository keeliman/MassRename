import os
import re
import configparser

# Load configurations from the .ini file
config = configparser.ConfigParser()
config.read('config.ini')

try:
    DIRECTORY_PATH = config['DEFAULT']['DIRECTORY_PATH']
    LAST_PUBLISHED = int(config['DEFAULT']['LAST_PUBLISHED'])
except KeyError:
    print("Error: Missing key in the configuration file.")
    exit()

def is_fully_numeric(filename):
    """Check if the filename (without extension) is fully numeric."""
    name, _ = os.path.splitext(filename)
    return name.isdigit()

def extract_numeric(filename):
    """Extract the number from the filename."""
    name, _ = os.path.splitext(filename)
    numbers = re.findall(r'\d+', name)
    return int(numbers[0]) if numbers else None

def rename_files_in_directory(directory, last_published):
    """Bulk rename files in the given directory."""
    # List of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Ensure all filenames are numeric
    for filename in files:
        if not is_fully_numeric(filename):
            num = extract_numeric(filename)
            if num is not None:
                new_name = str(num) + os.path.splitext(filename)[1]
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            else:
                print(f"Error: Unable to parse the file number from {filename}")
                return

    # Ensure videos are numbered starting from 1
    numbers = sorted([int(os.path.splitext(f)[0]) for f in files])
    if numbers[0] != 1:
        print("Error: Videos are not numbered starting from 1.")
        return

    # Rename files by incrementing with the last published number
    for filename in files:
        num = int(os.path.splitext(filename)[0])
        new_name = str(num + last_published) + os.path.splitext(filename)[1]
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

    print("Renaming completed successfully!")

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY_PATH):
        print(f"Error: The directory {DIRECTORY_PATH} does not exist.")
        exit()

    try:
        rename_files_in_directory(DIRECTORY_PATH, LAST_PUBLISHED)
    except Exception as e:
        print(f"An error occurred: {e}")
